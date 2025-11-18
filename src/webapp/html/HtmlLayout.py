#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlLayout.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# Copyright (C) 2025 Bruno Contreras Moreira and Joan Sarria
# (terms of use can be found within the distributed LICENSE file).

from components.HtmlComponents import HtmlComponents

from HtmlLayoutBarleymap import HtmlLayoutBarleymap

PREFIX_UI_CTRLS_ALIGN = "align"
PREFIX_UI_CTRLS_GRAPH = "graph"
PREFIX_UI_CTRLS_FIND = "find"
PREFIX_UI_CTRLS_LOCATE = "locate"

class HtmlLayout(object):
    _base_url = None
    _app_google_analytics_id = ""
    
    def __init__(self, base_url, app_google_analytics_id):
        self._base_url = base_url
        self._app_google_analytics_id = app_google_analytics_id
    
    ## Basic layout methods
    ##
    def html_head(self):
        output = []
        output.append(HtmlLayoutBarleymap.head(self._base_url))
        output.append(HtmlLayoutBarleymap.js_scripts(self._base_url, self._app_google_analytics_id))
        
        return "".join(output)  
    
    def html_head_maps(self):
        output = []
        output.append(HtmlLayoutBarleymap.head(self._base_url))
        output.append(HtmlLayoutBarleymap.js_scripts_maps(self._base_url, self._app_google_analytics_id))
        
        return "".join(output)
    
    def header(self):
        return HtmlLayoutBarleymap.title_header(self._base_url)
    
    def html_container(self, contents = []):
        return '<div id="container" style="margin:10px;">'+"".join(contents)+'</div> <!-- container -->'
    
    def footer(self):
        return HtmlLayoutBarleymap.footer()
    
    def html_end(self):
        return """
        </body>
        </html>
        """
    
    ## Methods which add content to the previous layout
    ##
    def main_text(self, citation):
        
        return HtmlLayoutBarleymap.main_text(citation, self._base_url, PREFIX_UI_CTRLS_ALIGN, PREFIX_UI_CTRLS_FIND,
                                             PREFIX_UI_CTRLS_LOCATE)
    
    def menu(self, citation):
        
        output = []
        output.append('<div id="menu">')
        output.append(HtmlLayoutBarleymap.text_menu(citation, self._base_url, show_last_changes = False))
        output.append('</div>')
        
        return "".join(output)
    
    ## Methods for specific contents
    ##
    def help(self):
        return HtmlComponents.help(self._base_url)
    
    def align_components(self, align_form, maps_config):
        
        align_components = HtmlComponents.align(self._base_url, align_form, PREFIX_UI_CTRLS_ALIGN,
                                                maps_config)
        
        return align_components

    def graph_components(self, align_form, maps_config):

        graph_components = HtmlComponents.graph(self._base_url, align_form, PREFIX_UI_CTRLS_GRAPH,
                                                maps_config)

        return graph_components
    
    def find_components(self, find_form, maps_config):
        
        find_components = HtmlComponents.find(self._base_url, find_form, PREFIX_UI_CTRLS_FIND,
                                              maps_config)
        
        return find_components
    
    def locate_components(self, form, maps_config):
        
        find_components = HtmlComponents.locate(self._base_url, form, PREFIX_UI_CTRLS_LOCATE,
                                              maps_config)
        
        return find_components

## END
