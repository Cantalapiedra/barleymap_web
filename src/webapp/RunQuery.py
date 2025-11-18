#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RunQuery.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# Copyright (C) 2025 Bruno Contreras Moreira and Joan Sarria
# (terms of use can be found within the distributed LICENSE file).

import sys, traceback
import cherrypy

from barleymapcore.db.PathsConfig import PathsConfig
from barleymapcore.m2p_exception import m2pException

from html.HtmlLayout import HtmlLayout

from FormsFactory import FormsFactory
from Bmap import Bmap, FIND_ACTION, ALIGN_ACTION, LOCATE_ACTION

DEFAULT_SORT_PARAM = "map default"
EMAIL_CONF = "EMAIL_CONF"
APP_NAME = "APP_NAME"
N_THREADS = "N_THREADS"
MAX_QUERIES = "MAX_QUERIES"
APP_GOOGLE_ANALYTICS_ID = "APP_GOOGLE_ANALYTICS_ID"

class Root():
    
    MOUNT_POINT = None
    PATHS_CONFIG = None
    
    VERBOSE = False
    
    def __init__(self, MOUNT_POINT, PATHS_CONFIG, VERBOSE):
        self.MOUNT_POINT = MOUNT_POINT
        self.PATHS_CONFIG = PATHS_CONFIG
        self.VERBOSE = VERBOSE
    
    def _get_html_layout(self, bmap_settings):
        return HtmlLayout(self.MOUNT_POINT, bmap_settings[APP_GOOGLE_ANALYTICS_ID])
    
    # Index method for direct requests from outside barleymap by url
    # For example, T3 or GrainGenes links
    # Maybe, this could be implemented as REST API in the future
    @cherrypy.expose
    def index(self, action = "", input_query = "", input_multiple = "", input_sort = "", input_genes = "",
              load_annot = "", genes_window = "",
              input_maps = "", send_email = "", email_to = ""):
        
        # GET /barleymap/mapmarkers/index?load_annot=1&genes_window=2.0&input_query=owbGBS1718
        # GET /barleymap/mapmarkers/index?load_annot=1&genes_window=2.0&input_query=12_30588
        
        sys.stderr.write("server.py: GET request to /mapmarkers/index\n")
        
        action = "index"
        query = input_query
        multiple = "1"
        sort = "bp"
        show_markers = "1"
        show_genes = "1"
        show_anchored = "0"
        show_main = "1"
        show_how = "1"
        extend = "1"
        extend_cm = 50000
        extend_bp = 50000
        maps = "morexv3" # so that all will be used
        send_email = "0"
        email_to = ""
        user_file = None
        
        try:
            bmap_settings = cherrypy.request.app.config['bmapsettings']
            
            form = FormsFactory.get_find_form_new(query, multiple, sort,
                                                       show_markers, show_genes, show_anchored,
                                                       show_main, show_how,
                                                       extend, extend_cm, extend_bp,
                                                       maps, send_email, email_to, user_file)
            
            form.set_action(action)
            form.set_session(cherrypy.session)
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            app_name = bmap_settings[APP_NAME]
            n_threads = bmap_settings[N_THREADS]
            max_queries = bmap_settings[MAX_QUERIES]
            
            bmap = Bmap(paths_config, DEFAULT_SORT_PARAM, max_queries, FIND_ACTION, n_threads, app_name, self.VERBOSE)
            
            results = bmap.find(form)
            
            csv_files = bmap.csv_files(results, form)
            
            output = bmap.output(results, form, self._get_html_layout(bmap_settings), csv_files)
            
            email_conf = bmap_settings[EMAIL_CONF]
            
            bmap.email(form, csv_files, email_conf)
            
        except m2pException as m2pe:
            sys.stderr.write(str(m2pe)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = str(m2pe)
            
        except Exception, e:
            sys.stderr.write(str(e)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = "There was a server error. Please, contact with barleymap web application adminitrators."
        
        return output
    
    @cherrypy.expose
    def find(self, action = "", query = "", multiple = "", sort = "",
             show_markers = "", show_genes = "", show_anchored = "",
             show_main = "", show_how = "",
             load_annot = "", extend = "", extend_cm = "", extend_bp = "",
             maps = "", send_email = "", email_to = "", user_file = None):
        
        sys.stderr.write("server.py: request to /mapmarkers/find\n")
        
        try:
            bmap_settings = cherrypy.request.app.config['bmapsettings']
            
            form = FormsFactory.get_find_form_new(query, multiple, sort,
                                                       show_markers, show_genes, show_anchored,
                                                       show_main, show_how,
                                                       extend, extend_cm, extend_bp,
                                                       maps, send_email, email_to, user_file)
            
            form.set_session(cherrypy.session)
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            app_name = bmap_settings[APP_NAME]
            n_threads = bmap_settings[N_THREADS]
            max_queries = bmap_settings[MAX_QUERIES]
            
            bmap = Bmap(paths_config, DEFAULT_SORT_PARAM, max_queries, FIND_ACTION, n_threads, app_name, self.VERBOSE)
            
            results = bmap.find(form)
            
            csv_files = bmap.csv_files(results, form)
            
            output = bmap.output(results, form, self._get_html_layout(bmap_settings), csv_files)
            
            email_conf = bmap_settings[EMAIL_CONF]
            
            bmap.email(form, csv_files, email_conf)
            
        except m2pException as m2pe:
            sys.stderr.write(str(m2pe)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = str(m2pe)
            
        except Exception, e:
            sys.stderr.write(str(e)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = "There was a server error. Please, contact with barleymap web application adminitrators."
        
        return output
    
    @cherrypy.expose
    def align(self, action = "", query = "", multiple = "", sort = "",
              show_markers = "", show_genes = "", show_anchored = "",
              show_main = "", show_how = "",
              load_annot = "", extend = "", extend_cm = "", extend_bp = "",
              maps = "", send_email = "", email_to = "", user_file = None,
              aligner = "", threshold_id = "", threshold_cov = ""):
        
        sys.stderr.write("server.py: request to /mapmarkers/align\n")
        
        try:
            bmap_settings = cherrypy.request.app.config['bmapsettings']
            
            form = FormsFactory.get_align_form_new(query, multiple, sort,
                                                   show_markers, show_genes, show_anchored,
                                                   show_main, show_how,
                                                   extend, extend_cm, extend_bp,
                                                   maps, send_email, email_to, user_file,
                                                     aligner, threshold_id, threshold_cov)
            
            form.set_session(cherrypy.session)
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            app_name = bmap_settings[APP_NAME]
            n_threads = bmap_settings[N_THREADS]
            max_queries = bmap_settings[MAX_QUERIES]
            
            bmap = Bmap(paths_config, DEFAULT_SORT_PARAM, max_queries, ALIGN_ACTION, n_threads, app_name, self.VERBOSE)
            
            results = bmap.align(form)
            
            csv_files = bmap.csv_files(results, form)
            
            output = bmap.output(results, form, self._get_html_layout(bmap_settings), csv_files)
            
            email_conf = bmap_settings[EMAIL_CONF]
            
            bmap.email(form, csv_files, email_conf)
        
        except m2pException as m2pe:
            sys.stderr.write(str(m2pe)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = str(m2pe)
            
        except Exception, e:
            sys.stderr.write(str(e)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = "There was a server error. Please, contact with barleymap web application adminitrators."
        
        return output
    
    @cherrypy.expose
    def graph(self, action = "", query = "", multiple = "", sort = "",
              show_markers = "", show_genes = "", show_anchored = "",
              show_main = "", show_how = "",
              load_annot = "", extend = "", extend_cm = "", extend_bp = "",
              maps = "", send_email = "", email_to = "", user_file = None,
              aligner = "", threshold_id = "", threshold_cov = ""):

        sys.stderr.write("server.py: request to /mapmarkers/graph\n")

        try:
            bmap_settings = cherrypy.request.app.config['bmapsettings']

            form = FormsFactory.get_graph_form_new(query, multiple, sort,
                                                   show_markers, show_genes, show_anchored,
                                                   show_main, show_how,
                                                   extend, extend_cm, extend_bp,
                                                   maps, send_email, email_to, user_file,
                                                     aligner, threshold_id, threshold_cov)

            form.set_session(cherrypy.session)

            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])

            app_name = bmap_settings[APP_NAME]
            n_threads = bmap_settings[N_THREADS]
            max_queries = bmap_settings[MAX_QUERIES]

            bmap = Bmap(paths_config, DEFAULT_SORT_PARAM, max_queries, ALIGN_ACTION, n_threads, app_name, self.VERBOSE)

            results = bmap.align(form)

            csv_files = bmap.csv_files(results, form)

            output = bmap.output(results, form, self._get_html_layout(bmap_settings), csv_files)

            email_conf = bmap_settings[EMAIL_CONF]

            bmap.email(form, csv_files, email_conf)

        except m2pException as m2pe:
            sys.stderr.write(str(m2pe)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = str(m2pe)

        except Exception, e:
            sys.stderr.write(str(e)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = "There was a server error. Please, contact with PrunusMap web application administrators."

        return output

    @cherrypy.expose
    def locate(self, action = "", query = "", multiple = "", sort = "",
             show_markers = "", show_genes = "", show_anchored = "",
             show_main = "", show_how = "",
             load_annot = "", extend = "", extend_cm = "", extend_bp = "",
             maps = "", send_email = "", email_to = "", user_file = None):
        
        sys.stderr.write("server.py: request to /mapmarkers/locate\n")
        
        try:
            bmap_settings = cherrypy.request.app.config['bmapsettings']
            
            form = FormsFactory.get_locate_form_new(query, multiple, sort,
                                                       show_markers, show_genes, show_anchored,
                                                       show_main, show_how,
                                                       extend, extend_cm, extend_bp,
                                                       maps, send_email, email_to, user_file)
            
            form.set_session(cherrypy.session)
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            app_name = bmap_settings[APP_NAME]
            n_threads = bmap_settings[N_THREADS]
            max_queries = bmap_settings[MAX_QUERIES]
            
            bmap = Bmap(paths_config, DEFAULT_SORT_PARAM, max_queries, LOCATE_ACTION, n_threads, app_name, self.VERBOSE)
            
            results = bmap.locate(form)
            
            csv_files = bmap.csv_files(results, form)
            
            output = bmap.output(results, form, self._get_html_layout(bmap_settings), csv_files)
            
            email_conf = bmap_settings[EMAIL_CONF]
            
            bmap.email(form, csv_files, email_conf)
        
        except m2pException as m2pe:
            sys.stderr.write(str(m2pe)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = str(m2pe)
            
        except Exception, e:
            sys.stderr.write(str(e)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = "There was a server error. Please, contact with barleymap web application adminitrators."
        
        return output
    
     # Index method for direct requests from outside barleymap by url
    # For example, T3 or GrainGenes links
    # Maybe, this could be implemented as REST API in the future
    #@cherrypy.expose
    #def index(self, action = "", input_query = "", input_multiple = "", input_sort = "", input_genes = "",
    #          load_annot = "", genes_window = "",
    #          input_maps = "", send_email = "", email_to = ""):
    #    
    #    sys.stderr.write("server.py: request to T3 links\n")
    #    
    #    verbose_param = self.VERBOSE
    #    
    #    #config_path_dict = read_paths("paths.conf") # data_utils.read_paths
    #    paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
    #    __app_path = paths_config.get_app_path()#config_path_dict["app_path"]
    #    
    #    # Load all configured maps
    #    maps_conf_file = paths_config.get_maps_path()#__app_path+"conf/maps.conf"
    #    (maps_names, maps_ids) = load_data(maps_conf_file, verbose = verbose_param) # data_utils.load_data
    #    if len(maps_names) > 1:
    #        input_maps = maps_names.split(",")
    #    else:
    #        input_maps = maps_names
    #    
    #    # Genes information: on marker
    #    input_genes = "marker"
    #    input_extend = "1"
    #    user_file = None
    #    
    #    output = self.find(input_query, input_multiple, input_sort, input_genes,
    #                      load_annot, input_exted, genes_window, genes_window,
    #                      input_maps, send_email, email_to, user_file)
    #    
    #    return output
    
## END
