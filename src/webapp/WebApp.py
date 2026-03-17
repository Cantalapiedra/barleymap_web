#!/usr/bin/env python
# -*- coding: utf-8 -*-

# WebApp.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# Copyright (C) 2025 Bruno Contreras Moreira and Joan Sarria
# (terms of use can be found within the distributed LICENSE file).

import sys, traceback
import cherrypy

from barleymapcore.db.ConfigBase import ConfigBase
from barleymapcore.db.PathsConfig import PathsConfig
from barleymapcore.db.MapsConfig import MapsConfig
from barleymapcore.db.GraphsConfig import GraphsConfig
from barleymapcore.db.DatabasesConfig import DatabasesConfig
from barleymapcore.m2p_exception import m2pException

from html.HtmlLayout import HtmlLayout

from FormsFactory import FormsFactory

########## MAIL SERVER
# check file in /home/barleymap/email/

DEFAULT_THRESHOLD_ID = "DEFAULT_THRESHOLD_ID"
DEFAULT_THRESHOLD_COV = "DEFAULT_THRESHOLD_COV"
DEFAULT_ALIGNER = "DEFAULT_ALIGNER"
DEFAULT_ALIGNER_GRAPH = "DEFAULT_ALIGNER_GRAPH"
DEFAULT_MAPS = "DEFAULT_MAPS"
DEFAULT_GRAPHS = "DEFAULT_GRAPHS"
DEFAULT_GENES_WINDOW_CM = "DEFAULT_GENES_WINDOW_CM"
DEFAULT_GENES_WINDOW_BP = "DEFAULT_GENES_WINDOW_BP"
APP_GOOGLE_ANALYTICS_ID = "APP_GOOGLE_ANALYTICS_ID"

class Root():
    
    MOUNT_POINT = None
    PATHS_CONFIG = None
    
    VERBOSE = False
    
    def __init__(self, MOUNT_POINT, PATHS_CONFIG, VERBOSE):
        self.MOUNT_POINT = MOUNT_POINT
        self.PATHS_CONFIG = PATHS_CONFIG
        self.VERBOSE = VERBOSE
        return
    
    def _get_html_layout(self, bmap_settings):
        
        return HtmlLayout(self.MOUNT_POINT, bmap_settings[APP_GOOGLE_ANALYTICS_ID])
    
    @cherrypy.expose
    def index(self):
        try:
            sys.stderr.write("server.py: request to /index\n")
            
            bmap_settings = cherrypy.request.app.config['bmapsettings']
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            html_layout = self._get_html_layout(bmap_settings)
            
            citation = paths_config.get_citation().replace("_", " ")#[PathsConfig._CITATION].replace("_", " ")
            
            contents = [html_layout.main_text(citation)]
            
            output = "".join([html_layout.html_head(),
                             html_layout.header(),
                             html_layout.html_container(contents),
                             html_layout.footer(),
                             html_layout.html_end()])
        
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
    def find(self):
        sys.stderr.write("server.py: request to /find/\n")
        
        try:
            bmap_settings = cherrypy.request.app.config['bmapsettings']
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            html_layout = self._get_html_layout(bmap_settings)
            
            app_path = paths_config.get_app_path()#paths_config[PathsConfig._APP_PATH]
            maps_conf_file = app_path+ConfigBase.MAPS_CONF
            maps_config = MapsConfig(maps_conf_file, self.VERBOSE)
            
            session = cherrypy.session
            if session.get('session_token'):
                find_form = FormsFactory.get_find_form_session(session)
                
                if find_form.get_action() == "index":
                    window_cm = bmap_settings[DEFAULT_GENES_WINDOW_CM]
                    window_bp = bmap_settings[DEFAULT_GENES_WINDOW_BP]
                    maps = bmap_settings[DEFAULT_MAPS]
                    
                    find_form = FormsFactory.get_find_form_empty(window_cm, window_bp, maps)
                    
            else:
                window_cm = bmap_settings[DEFAULT_GENES_WINDOW_CM]
                window_bp = bmap_settings[DEFAULT_GENES_WINDOW_BP]
                maps = bmap_settings[DEFAULT_MAPS]
                
                find_form = FormsFactory.get_find_form_empty(window_cm, window_bp, maps)
            
            find_form.get_query()
            
            find_component = html_layout.find_components(find_form, maps_config)
            
            citation = paths_config.get_citation().replace("_", " ")#paths_config[PathsConfig._CITATION].replace("_", " ")
            
            contents = [html_layout.menu(citation),
                        find_component]
            
            output = "".join([html_layout.html_head(),
                              html_layout.header(),
                              html_layout.html_container(contents),
                              html_layout.footer(),
                              html_layout.html_end()])
        
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
    def align(self):
        sys.stderr.write("server.py: request to /align/\n")
        
        try:
            bmap_settings = cherrypy.request.app.config['bmapsettings']
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            html_layout = self._get_html_layout(bmap_settings)
            
            app_path = paths_config.get_app_path()#[PathsConfig._APP_PATH]
            maps_conf_file = app_path+ConfigBase.MAPS_CONF
            maps_config = MapsConfig(maps_conf_file, self.VERBOSE)
            
            session = cherrypy.session
            
            aligner = bmap_settings[DEFAULT_ALIGNER]
            threshold_id = bmap_settings[DEFAULT_THRESHOLD_ID]
            threshold_cov = bmap_settings[DEFAULT_THRESHOLD_COV]
            
            if session.get('session_token'):
                align_form = FormsFactory.get_align_form_session(session, aligner, threshold_id, threshold_cov)
                
                if align_form.get_action() == "index":
                    window_cm = bmap_settings[DEFAULT_GENES_WINDOW_CM]
                    window_bp = bmap_settings[DEFAULT_GENES_WINDOW_BP]
                    maps = bmap_settings[DEFAULT_MAPS]
                    
                    align_form = FormsFactory.get_align_form_empty(window_cm, window_bp, maps, aligner, threshold_id, threshold_cov)
                    
            else:
                window_cm = bmap_settings[DEFAULT_GENES_WINDOW_CM]
                window_bp = bmap_settings[DEFAULT_GENES_WINDOW_BP]
                maps = bmap_settings[DEFAULT_MAPS]
                
                align_form = FormsFactory.get_align_form_empty(window_cm, window_bp, maps, aligner, threshold_id, threshold_cov)
            
            align_component = html_layout.align_components(align_form, maps_config)
            
            citation = paths_config.get_citation().replace("_", " ")#[PathsConfig._CITATION].replace("_", " ")
            
            contents = [html_layout.menu(citation),
                        align_component]
            
            output = "".join([html_layout.html_head(),
                              html_layout.header(),
                              html_layout.html_container(contents),
                              html_layout.footer(),
                              html_layout.html_end()])  
        
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
    def graph(self):
        sys.stderr.write("server.py: request to /graph/\n")
                        
        try:
            bmap_settings = cherrypy.request.app.config['bmapsettings']
                              
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
                              
            html_layout = self._get_html_layout(bmap_settings)

            app_path = paths_config.get_app_path()#[PathsConfig._APP_PATH]
            graphs_conf_file = app_path+ConfigBase.GRAPHS_CONF
            graphs_config = GraphsConfig(graphs_conf_file, self.VERBOSE)

            session = cherrypy.session
            
            aligner = bmap_settings[DEFAULT_ALIGNER_GRAPH]
            threshold_id = bmap_settings[DEFAULT_THRESHOLD_ID]
            threshold_cov = bmap_settings[DEFAULT_THRESHOLD_COV]

            if session.get('session_token'):
                graph_form = FormsFactory.get_graph_form_session(session, aligner, threshold_id, threshold_cov)

                if graph_form.get_action() == "index":
                    window_cm = bmap_settings[DEFAULT_GENES_WINDOW_CM]
                    window_bp = bmap_settings[DEFAULT_GENES_WINDOW_BP]
                    graphs = bmap_settings[DEFAULT_GRAPHS]

                    graph_form = FormsFactory.get_graph_form_empty(window_cm, window_bp, graphs, aligner, 
                                                                   threshold_id, threshold_cov)

            else:
                window_cm = bmap_settings[DEFAULT_GENES_WINDOW_CM]
                window_bp = bmap_settings[DEFAULT_GENES_WINDOW_BP]
                graphs = bmap_settings[DEFAULT_GRAPHS]

                graph_form = FormsFactory.get_graph_form_empty(window_cm, window_bp, graphs, aligner, threshold_id, threshold_cov)

            graph_component = html_layout.graph_components(graph_form, graphs_config)

            citation = paths_config.get_citation().replace("_", " ")#[PathsConfig._CITATION].replace("_", " ")

            contents = [html_layout.menu(citation),
                        graph_component]

            output = "".join([html_layout.html_head(),
                              html_layout.header(),
                              html_layout.html_container(contents),
                              html_layout.footer(),
                              html_layout.html_end()])  

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
    def locate(self):
        sys.stderr.write("server.py: request to /locate/\n")
        
        try:
            bmap_settings = cherrypy.request.app.config['bmapsettings']
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            html_layout = self._get_html_layout(bmap_settings)
            
            app_path = paths_config.get_app_path()#[PathsConfig._APP_PATH]
            maps_conf_file = app_path+ConfigBase.MAPS_CONF
            maps_config = MapsConfig(maps_conf_file, self.VERBOSE)
            
            session = cherrypy.session
            if session.get('session_token'):
                form = FormsFactory.get_locate_form_session(session)
                
                if form.get_action() == "index":
                    window_cm = bmap_settings[DEFAULT_GENES_WINDOW_CM]
                    window_bp = bmap_settings[DEFAULT_GENES_WINDOW_BP]
                    maps = bmap_settings[DEFAULT_MAPS]
                    
                    form = FormsFactory.get_locate_form_empty(window_cm, window_bp, maps)
                    
            else:
                window_cm = bmap_settings[DEFAULT_GENES_WINDOW_CM]
                window_bp = bmap_settings[DEFAULT_GENES_WINDOW_BP]
                maps = bmap_settings[DEFAULT_MAPS]
                
                form = FormsFactory.get_locate_form_empty(window_cm, window_bp, maps)
            
            form.get_query()
            
            # It should be the same layout as for the find page
            locate_component = html_layout.locate_components(form, maps_config)
            
            citation = paths_config.get_citation().replace("_", " ")#paths_config[PathsConfig._CITATION].replace("_", " ")
            
            contents = [html_layout.menu(citation),
                        locate_component]
            
            output = "".join([html_layout.html_head(),
                              html_layout.header(),
                              html_layout.html_container(contents),
                              html_layout.footer(),
                              html_layout.html_end()])
        
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
    def help(self):
        sys.stderr.write("server.py: request to /help/\n")
        
        try:
            bmap_settings = cherrypy.request.app.config['bmapsettings']
            
            paths_config = PathsConfig.from_dict(cherrypy.request.app.config[self.PATHS_CONFIG])
            
            html_layout = self._get_html_layout(bmap_settings)
            
            citation = paths_config.get_citation().replace("_", " ")#[PathsConfig._CITATION].replace("_", " ")
            
            contents = [html_layout.menu(citation),
                        html_layout.help()]
            
            output = "".join([html_layout.html_head(),
                              html_layout.header(),
                              html_layout.html_container(contents),
                              html_layout.footer(),
                              html_layout.html_end()])  
        
        except m2pException as m2pe:
            sys.stderr.write(str(m2pe)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = str(m2pe)
            
        except Exception, e:
            sys.stderr.write(str(e)+"\n")
            traceback.print_exc(file=sys.stderr)
            output = "There was a server error. Please, contact with barleymap web application adminitrators."
        
        return output

## END
