#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GraphsConfig.py is part of Barleymap.
# Copyright (C) 2025 Bruno Contreras, Joan Sarria
# (terms of use can be found within the distributed LICENSE file).

import sys

from barleymapcore.m2p_exception import m2pException
from barleymapcore.utils.data_utils import load_conf

# Fields in graphs.conf file
GRAPH_NAME = 0
GRAPH_ID = 1
GRAPH_MAP = 2

class GraphsConfig(object):
    
    _config_file = ""
    _verbose = False
    _config_dict = {} # dict with data from config file (default: conf/graphs.conf)
    _config_list = []

    def __init__(self, config_file, verbose = True):
        self._config_file = config_file
        self._verbose = verbose
        self._load_config(config_file)
    
    def _load_config(self, config_file):
        self._config_dict = {}
        self._config_list = []
        conf_rows = load_conf(config_file, self._verbose) # data_utils.load_conf
        
        for conf_row in conf_rows:
            graph_id = conf_row[GRAPH_ID]
            graph_name = conf_row[GRAPH_NAME]
            graph_map = conf_row[GRAPH_MAP]
            
            self._config_dict[graph_id] = {GRAPH_NAME:graph_name, GRAPH_MAP:graph_map}
            self._config_list.append(graph_id)

    def get_config_file(self):
        return self._config_file 

    def get_graphs(self):
        return self._config_dict
    
    def get_graph(self, database_id):
        if self.database_exists(database_id):
            return self._config_dict[database_id]
        else:
            return None
    
    def get_graph_name(self, database_id):
        if self.database_exists(database_id):
            return self._config_dict[database_id][GRAPH_NAME]
        else:
            return database_id
    
    def get_graph_map(self, database_id):
        if self.database_exists(database_id):
            return self._config_dict[database_id][GRAPH_MAP]
        else:
            return None
  
    # for compatibility
    def get_database_type(self, database_id):
        if self.database_exists(database_id):
            return 'std'
        else:
            return None    

     # Return tuples (graph_id, graph_name)
    def get_graphs_tuples(self, ):
        graphs_tuples = []

        for graph_id in self._config_list:
            graphs_tuples.append((graph_id, self._config_dict[graph_id][GRAPH_NAME]))

        return graphs_tuples

    def get_graph_config(self, graph_id):
        if graph_id in self._config_dict:#self._config_dict:
            graph_config = self._config_dict[graph_id]
        else:
            sys.stderr.write("WARNING: GraphsConfig: graph ID "+graph_id+" is not in config file.\n")

        return graph_config

    def get_graphs_ids(self, databases_names = None):
        databases_ids = []
  
        if databases_names:
            # Doing this in a loop to conserve order
            for database_name in databases_names:
                found = False
                for database in self._config_dict:
                    if self._config_dict[database][GRAPH_NAME] == database_name:
                        databases_ids.append(database)
                        found = True
                        break
                
                if not found:
                    sys.stderr.write("WARNING: GraphsConfig: database name "+database_name+" not found in config.\n")
        else:
            databases_ids = self._config_dict.keys()
        
        return databases_ids
    
    def get_graphs_names(self, databases_ids = None):
        databases_names = []

        if databases_ids:
            for database in databases_ids:
                found = False
                if database in self._config_dict:
                    databases_names.append(self._config_dict[database][GRAPH_NAME])
                    found = True
                    break

            if not found:
                sys.stderr.write("WARNING: GraphsConfig: database ID "+database+" not found in config.\n")
                databases_names.append(database)
        
        else:
            for graph_id in self._config_list:
                databases_names.append(self._config_dict[graph_id][GRAPH_NAME])

        return databases_names
   
    # compatibility
    def database_exists(self, database):
        return database in self._config_dict


## END
