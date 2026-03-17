#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OutputMaps.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys

from HtmlWriter import HtmlWriter

class OutputMaps(object):
    
    _paths_config = None
    _app_name = None
    _html_layout = None
    
    def __init__(self, paths_config, app_name, html_layout):
        self._paths_config = paths_config
        self._app_name = app_name
        self._html_layout = html_layout
        self._html_writer = HtmlWriter("/"+self._app_name,
                                       self._paths_config.get_tmp_files_path(),
                                       self._paths_config.get_genmap_path(),
                                       self._paths_config.get_maps_path())
    
    def _output_map(self, mapping_results, form, map_links_dict, map_csv_files):
        html_writer = self._html_writer
        
        multiple_param = form.get_multiple()
        csv_file_name = map_csv_files.get_mapped()
        
        html_writer.output_genetic_map(map_links_dict, mapping_results, multiple_param, csv_file_name)
        
        return
    
    def _output_map_with_markers(self, mapping_results, form, map_links_dict, map_csv_files):
        html_writer = self._html_writer
        
        multiple_param = form.get_multiple()
        csv_file_name = map_csv_files.get_map_with_markers()
        
        html_writer.output_map_with_markers(map_links_dict, mapping_results, multiple_param, csv_file_name)
        
        return
    
    def _output_map_with_genes(self, mapping_results, form, map_links_dict, map_csv_files):
        html_writer = self._html_writer
        
        multiple_param = form.get_multiple()
        csv_file_name = map_csv_files.get_map_with_genes()
        
        annotator = mapping_results.get_annotator()
        html_writer.output_map_with_genes(map_links_dict, mapping_results, multiple_param, csv_file_name, annotator)
        
        return
    
    def _output_map_with_anchored(self, mapping_results, form, map_links_dict, map_csv_files):
        html_writer = self._html_writer
        
        multiple_param = form.get_multiple()
        csv_file_name = map_csv_files.get_map_with_anchored()
        
        html_writer.output_map_with_anchored(map_links_dict, mapping_results, multiple_param, csv_file_name)
        
        return
    
    def _output_unmapped(self, mapping_results, map_links_dict, map_csv_files):
        html_writer = self._html_writer
        
        if mapping_results.get_unmapped():
            csv_file_name = map_csv_files.get_unmapped()
            html_writer.output_unmapped(map_links_dict, mapping_results, csv_file_name) 
        
        return
    
    def _output_unaligned(self, mapping_results, map_links_dict, map_csv_files):
        html_writer = self._html_writer
        
        csv_file_name = map_csv_files.get_unaligned()
        
        html_writer.output_unaligned(map_links_dict, mapping_results, csv_file_name)
        
        return
    
    def output(self, all_mapping_results, form, csv_files):
        
        paths_config = self._paths_config
        html_layout = self._html_layout
        action = form.get_action()
        
        html_writer = self._html_writer
        html_writer.init_output_buffer()
        
        #html_writer.output_text(html_layout.html_head())
        html_writer.output_text(html_layout.html_head_maps())
        html_writer.output_text(html_layout.header())
        html_writer.output_text('<section id="body_section">')
        
        
        html_writer.output_text("<strong>please cite</strong> "+
                                "<a href='http://link.springer.com/article/10.1007%2Fs11032-015-0253-1' target='_blank' style='text-decoration:none;font-size:small;'>"+
                                paths_config.get_citation().replace("_", " ")+
                                "</a>"+
                                "<br/><br/>")
        
        html_writer.output_html_back_button(action)
        
        html_writer.output_text('<section id="results_section">')
        # TOP MENU
        if len(all_mapping_results) > 1:
            html_writer.output_top_menu(all_mapping_results)
        
        ################################## MAPS ########################
        ################################################################
        for mapping_results in all_mapping_results:
            
            map_config = mapping_results.get_map_config()
            map_id = map_config.get_id()
            
            map_csv_files = csv_files.get_map_csv_files(map_id)
            
            sys.stderr.write("Creating output for map... "+str(map_config.get_name())+"\n")
            
            map_links_dict = html_writer.output_map_menu(mapping_results, form)
            
            self._output_map(mapping_results, form, map_links_dict, map_csv_files)
            
            if form.get_show_markers() and mapping_results.get_map_with_markers():
                self._output_map_with_markers(mapping_results, form, map_links_dict, map_csv_files)
                
            if form.get_show_genes() and mapping_results.get_map_with_genes():
                self._output_map_with_genes(mapping_results, form, map_links_dict, map_csv_files)
                
            if form.get_show_anchored() and mapping_results.get_map_with_anchored():
                self._output_map_with_anchored(mapping_results, form, map_links_dict, map_csv_files)
            
            if mapping_results.get_unmapped(): self._output_unmapped(mapping_results, map_links_dict, map_csv_files)
            if mapping_results.get_unaligned(): self._output_unaligned(mapping_results, map_links_dict, map_csv_files)
            
            html_writer.output_text('<hr/>')
            
            sys.stderr.write("Output for map "+str(map_config.get_name())+" finished.\n")
        
        ################################################################
        html_writer.output_text('</section>') # results_section
        html_writer.output_html_back_button(action)
        html_writer.output_text('</section>') # body_section
        
        html_writer.output_text(html_layout.footer())
        html_writer.output_text(html_layout.html_end())#output_html_end()
        
        output_buffer = html_writer.get_output_buffer()
        
        return "".join(output_buffer)

## END
