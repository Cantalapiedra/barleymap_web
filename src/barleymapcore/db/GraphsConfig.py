#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GraphsConfig.py is part of Barleymap.
# Copyright (C)  2016  Carlos P Cantalapiedra.
# Copyright (C) 2025 Bruno Contreras Moreira and Joan Sarria
# (terms of use can be found within the distributed LICENSE file).

import sys

from barleymapcore.m2p_exception import m2pException
from barleymapcore.utils.data_utils import load_conf
from barleymapcore.maps.MapsBase import MapTypes

class GraphConfig(object):
    _name = ""
    _id = ""
    _map = ""
    
    def __init__(self, name, graph_id, map):
        
        self._name = name
        self._id = graph_id
        self._map = map
        
        return
    
    # These are wrappers to use the config_dict fields just within GraphConfig class
    def get_name(self):
        return self._name
    
    def get_id(self):
        return self._id
    
    def get_map(self):
        return self._map
    
class GraphsConfig(object):
    
    # Field number (space delimited)
    # in configuration file
    GRAPH_NAME = 0
    GRAPH_ID = 1
    MAP = 2

    _config_file = ""
    _verbose = False
    _config_dict = {} # dict with data from maps configuration file (default: conf/graphs.conf)
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
            
            graph_name = conf_row[self.GRAPH_NAME]
            graph_id = conf_row[self.GRAPH_ID]
            map = conf_row[self.MAP]
            
            graph_config = GraphConfig(graph_name, graph_id, map)
            
            self._config_dict[graph_id] = graph_config
            self._config_list.append(graph_id)
    
    def get_config_file(self):
        return self._config_file
    
    def get_graphs(self):
        return self._config_dict
    
    def get_graphs_list(self, ):
        return self._config_list
    
    # Return tuples (graph_id, graph_name)
    def get_graphs_tuples(self, ):
        graphs_tuples = []
        
        for graph_id in self._config_list:
            graphs_tuples.append((graph_id, self.get_graph_config(graph_id).get_name()))
        
        return graphs_tuples
    
    def get_graph_config(self, graph_id):        
        if graph_id in self._config_dict:#self._config_dict:
            graph_config = self._config_dict[graph_id]
        else:
            sys.stderr.write("WARNING: GraphsConfig: graph ID "+graph_id+" is not in config file.\n")
        
        return graph_config
    
    def get_graphs_names(self, graphs_ids):
        graphs_names = []
        
        for graph_id in graphs_ids:
            if graph_id in self._config_dict:
                graph_config = self.get_graph_config(graph_id)
                graphs_names.append(graph_config.get_name())
            else:
                sys.stderr.write("WARNING: GraphsConfig: graph ID "+graph_id+" not found in config.\n")
                graphs_names.append(graph_id)
        
        return graphs_names
    
    def get_graphs_ids(self, graphs_names = None):
        graphs_ids = []
        
        if graphs_names:
            # changing dict[id]-->name to dict[name]-->id
            # This means that both id and name must be unique in configuration
            
            graph_names_set = dict([
                                (self.get_graph_config(graph_id).get_name(),graph_id)
                                for graph_id in self.get_graphs()
                                ])
            
            # Doing this in a loop to conserve order
            for graph_name in graphs_names:
                if graph_name in graph_names_set:
                    graph_id = graph_names_set[graph_name]
                    graphs_ids.append(graph_id)
                else:
                    sys.stderr.write("GraphsConfig: graph name "+graph_name+" not found in config.\n")
        else:
            graphs_ids = self._config_dict.keys()
        
        return graphs_ids
    
## END
