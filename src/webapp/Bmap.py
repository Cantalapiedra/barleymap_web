#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bmap.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# Copyright (C) 2025 Bruno Contreras Moreira and Joan Sarria
# (terms of use can be found within the distributed LICENSE file).

import sys, tempfile, os, csv

from barleymapcore.db.ConfigBase import ConfigBase
from barleymapcore.db.MapsConfig import MapsConfig
from barleymapcore.db.DatasetsConfig import DatasetsConfig
from barleymapcore.db.DatabasesConfig import DatabasesConfig
from barleymapcore.alignment.AlignmentFacade import AlignmentFacade
from barleymapcore.datasets.DatasetsFacade import DatasetsFacade
from barleymapcore.annotators.GenesAnnotator import AnnotatorsFactory
from barleymapcore.maps.MapMarkers import MapMarkers
from barleymapcore.maps.MapsBase import MapTypes
from barleymapcore.maps.enrichment.MapEnricher import SHOW_ON_INTERVALS, SHOW_ON_MARKERS
from barleymapcore.output.CSVWriter import CSVWriter
from barleymapcore.m2p_exception import m2pException

from html.output.OutputMaps import OutputMaps

import m2p_mail

MAPS_CONF = ConfigBase.MAPS_CONF
DATABASES_CONF = ConfigBase.DATABASES_CONF
DATASETS_CONF = ConfigBase.DATASETS_CONF
DATASETS_ANNOTATION_CONF = ConfigBase.DATASETS_ANNOTATION_CONF
ANNOTATION_TYPES_CONF = ConfigBase.ANNOTATION_TYPES_CONF

FIND_ACTION = "find"
ALIGN_ACTION = "align"
LOCATE_ACTION = "locate"
GRAPH_ACTION = "graph"

class Bmap(object):
    _paths_config = None
    
    _default_sort = None
    _max_queries = None
    _action = None
    _n_threads = None
    _app_name = None
    
    _verbose = False
    
    def __init__(self, paths_config, default_sort, max_queries, action, n_threads, app_name, verbose = False):
        self._paths_config = paths_config
        self._default_sort = default_sort
        self._max_queries = max_queries
        self._action = action
        self._n_threads = n_threads
        self._app_name = app_name
        self._verbose = verbose
    
    def __tmpfile_from_list(self, input_list, tmp_dir):
        input_file_name = ""
        input_file = None
        try:
            (file_desc, input_file_name) = tempfile.mkstemp(suffix="_mapm", dir=tmp_dir)
            input_file = os.fdopen(file_desc, 'w')
            
            for array_line in input_list:
                input_file.write(array_line+"\n")
            input_file.close()
            
        except Exception:
            raise
        finally:
            if input_file:
                input_file.close()
        
        return input_file_name
    
    def __check_input_query(self, input_lines):
        
        action = self._action
        ## Preprocessing and format control of input data (either uploaded file and text area)
        # FASTA FORMAT
        if input_lines[0].startswith(">"):
            if action == ALIGN_ACTION or action == GRAPH_ACTION:
                
                ## LIMIT OF QUERIES ACCEPTED IN THE WEB 20140529
                num_queries = len([x for x in input_lines if x.startswith(">")])
                
                max_queries = self._max_queries#ResourcesMng.get_max_queries()
                
                if num_queries > max_queries:
                    if self._verbose: sys.stderr.write("NUM QUERIES ******************** "+str(num_queries)+" ---- "+str(max_queries)+"\n")
                    raise m2pException("The web application only accepts currently "+str(max_queries)+" in the align/graph modes.\
                                       We counted "+str(num_queries)+" in your request.\
                                       We would recommend you to use the standalone version.")
                
                # OK
                
            elif action == FIND_ACTION or action == LOCATE_ACTION:
                raise m2pException("Find and locate actions require a list of identifiers. Avoid FASTA format (e.g. lines starting with \">\")") 
            else:
                raise m2pException("Unknown action requested.")
                
        # NO fasta format
        else:
            if action == ALIGN_ACTION or action == GRAPH_ACTION:
                raise m2pException("The input for "+ALIGN_ACTION+" action must be in FASTA format.")
            elif action == FIND_ACTION or action == LOCATE_ACTION:
                pass # OK
            else:
                raise m2pException("Unknown action requested.")
        
        return

    def __get_input_file(self, input_form):
        
        query = input_form.get_query()
        user_file = input_form.get_user_file()
        
        if ((not query) or (query.strip() == "")) and (not user_file or not user_file.file):
            raise m2pException("No input data provided.")
        
        if user_file and user_file.file: # Uploaded file
            input_lines = []
            for line in user_file.file:
                input_lines.append(line)
        else: # Text Area
            input_lines = query.strip().split("\n")
        
        # Check input data
        self.__check_input_query(input_lines)
        
        # Input tmp file
        tmp_dir = self._paths_config.get_tmp_files_path()
        input_file_name = self.__tmpfile_from_list(input_lines, tmp_dir)
        
        return input_file_name
    
    ##
    def _get_annotator(self, show_genes):
        if show_genes:
            paths_config = self._paths_config
            __app_path = paths_config.get_app_path()
            ## Load annotation config
            dsannot_conf_file = __app_path+DATASETS_ANNOTATION_CONF
            anntypes_conf_file = __app_path+ANNOTATION_TYPES_CONF
            annot_path = paths_config.get_annot_path()
            
            annotator = AnnotatorsFactory.get_annotator(dsannot_conf_file, anntypes_conf_file, annot_path, self._verbose)
        else:
            annotator = None
        
        return annotator
    
    ##
    def find(self, find_form):
        
        input_file_name = self.__get_input_file(find_form)
        
        ## Configuration files and paths
        paths_config = self._paths_config
        __app_path = paths_config.get_app_path()
        
        # Datasets
        datasets_conf_file = __app_path+DATASETS_CONF
        datasets_config = DatasetsConfig(datasets_conf_file, self._verbose)
        datasets_ids = datasets_config.get_datasets_list() #datasets_config.get_datasets().keys()
        
        # Maps
        maps_conf_file = __app_path+MAPS_CONF
        maps_config = MapsConfig(maps_conf_file, self._verbose)
        if find_form.get_maps():
            maps = find_form.get_maps()
            
            if isinstance(maps, basestring): maps = [maps]
            
            maps_names = maps_config.get_maps_names(maps)
            maps_ids = maps#maps_config.get_maps_ids(maps_names.strip().split(","))
        else:
            maps_ids = maps_config.get_maps().keys()
            maps_names = ",".join(maps_config.get_maps_names(maps_ids))
        
        maps_path = paths_config.get_maps_path() #__app_path+config_path_dict["maps_path"]
        
        # Datasets
        datasets_conf_file = __app_path+DATASETS_CONF
        datasets_config = DatasetsConfig(datasets_conf_file, self._verbose)
        
        ############ ALIGNMENTS - DATASETS
        # Load configuration paths
        datasets_path = paths_config.get_datasets_path() #__app_path+config_path_dict["datasets_path"]
        datasets_facade = DatasetsFacade(datasets_config, datasets_path, maps_path, verbose = self._verbose)
        
        ########### Create maps
        ###########
        sort_param = find_form.get_sort()
        multiple_param = True if find_form.get_multiple()=="1" else False
        show_markers = True if find_form.get_show_markers()=="1" else False
        show_genes = True if find_form.get_show_genes()=="1" else False
        show_anchored = True if find_form.get_show_anchored()=="1" else False
        show_main = True if find_form.get_show_main() == "1" else False
        show_how = SHOW_ON_MARKERS if find_form.get_show_how() == "1" else SHOW_ON_INTERVALS
        collapsed_view = find_form.get_collapsed_view()
        constrain_fine_mapping = True
        
        all_mapping_results = []
        for map_id in maps_ids:
            sys.stderr.write("Bmap.find: Map "+map_id+"\n")
            map_config = maps_config.get_map_config(map_id)
            
            sort_by = map_config.check_sort_param(map_config, sort_param, self._default_sort)
            
            if find_form.get_extend() != "":
                if sort_by == MapTypes.MAP_SORT_PARAM_CM:
                    extend_window = float(find_form.get_extend_cm())
                elif sort_by == MapTypes.MAP_SORT_PARAM_BP:
                    extend_window = float(find_form.get_extend_bp())
            else:
                extend_window = 0
                
            mapMarkers = MapMarkers(maps_path, map_config, datasets_facade, self._verbose)
            
            mapMarkers.retrieve_mappings(input_file_name, datasets_ids,
                                        sort_by, multiple_param)
            
            #load_annot = True always
            # GenesAnnotator
            annotator = self._get_annotator(show_genes)
            
            if show_main:
                datasets_enrichment = map_config.get_main_datasets()
            else:
                datasets_enrichment = datasets_ids
            
            mapMarkers.enrichment(annotator, show_markers, show_genes, show_anchored, show_how,
                                  datasets_facade, datasets_enrichment, extend_window, collapsed_view, constrain_fine_mapping)
            
            mapping_results = mapMarkers.get_mapping_results()
            
            mapping_results.set_annotator(annotator)
            
            sys.stderr.write("Bmap.find: mapped num. of results: "+str(len(mapping_results.get_mapped()))+"\n")
            
            all_mapping_results.append(mapping_results)
            
        return all_mapping_results
    
    ##
    def align(self, align_form):
        
        input_file_name = self.__get_input_file(align_form)
        
        ## Configuration files and paths
        paths_config = self._paths_config
        __app_path = paths_config.get_app_path()
        
        # Maps
        maps_conf_file = __app_path+MAPS_CONF
        maps_config = MapsConfig(maps_conf_file)
        if align_form.get_maps():
            maps = align_form.get_maps()
            
            if isinstance(maps, basestring): maps = [maps]
            
            maps_names = maps_config.get_maps_names(maps)
            maps_ids = maps#maps_config.get_maps_ids(maps_names.strip().split(","))
        else:
            maps_ids = maps_config.get_maps().keys()
            maps_names = ",".join(maps_config.get_maps_names(maps_ids))
        
        maps_path = paths_config.get_maps_path() #__app_path+config_path_dict["maps_path"]
        
        ############# ALIGNMENTS - REFERENCES
        
        # Databases
        databases_conf_file = __app_path+DATABASES_CONF
        databases_config = DatabasesConfig(databases_conf_file, self._verbose)
        
        alignment_facade = AlignmentFacade(paths_config, verbose = self._verbose)
        
        ############ Pre-loading of some objects
        ############
        # DatasetsFacade
        # Datasets config
        datasets_conf_file = __app_path+DATASETS_CONF
        datasets_config = DatasetsConfig(datasets_conf_file)
        datasets_ids = datasets_config.get_datasets().keys()
        
        # Load DatasetsFacade
        datasets_path = paths_config.get_datasets_path() #__app_path+config_path_dict["datasets_path"]
        datasets_facade = DatasetsFacade(datasets_config, datasets_path, maps_path, verbose = self._verbose)
        
        # Temp directory
        tmp_files_dir = paths_config.get_tmp_files_path()
        
        ########### Create maps
        ###########
        sort_param = align_form.get_sort()
        multiple_param = True if align_form.get_multiple()=="1" else False
        show_markers = True if align_form.get_show_markers() == "1" else False
        show_genes = True if align_form.get_show_genes() == "1" else False
        show_anchored = True if align_form.get_show_anchored() == "1" else False
        show_main = True if align_form.get_show_main() == "1" else False
        show_how = SHOW_ON_MARKERS if align_form.get_show_how() == "1" else SHOW_ON_INTERVALS
        collapsed_view = align_form.get_collapsed_view()
        constrain_fine_mapping = True
        best_score = True
        
        aligner = align_form.get_aligner()
        if "," in aligner:
            aligner_list = aligner.strip().split(",")
        else:
            aligner_list = [aligner]
        
        sys.stderr.write("BMAP aligner_list: "+str(aligner_list)+"\n")
        
        threshold_id = float(align_form.get_threshold_id())
        threshold_cov = float(align_form.get_threshold_cov())
        
        all_mapping_results = []
        for map_id in maps_ids:
            sys.stderr.write("bmap_align: Map "+map_id+"\n")
            
            map_config = maps_config.get_map_config(map_id)
            databases_ids = map_config.get_db_list()
            
            sort_by = map_config.check_sort_param(map_config, sort_param, self._default_sort)
            
            if align_form.get_extend() != "":
                if sort_by == MapTypes.MAP_SORT_PARAM_CM:
                    extend_window = float(align_form.get_extend_cm())
                elif sort_by == MapTypes.MAP_SORT_PARAM_BP:
                    extend_window = float(align_form.get_extend_bp())
            else:
                extend_window = 0
            
            mapMarkers = MapMarkers(maps_path, map_config, alignment_facade, self._verbose)
            
            mapMarkers.perform_mappings(input_file_name, databases_ids, databases_config, aligner_list,
                                        threshold_id, threshold_cov, self._n_threads,
                                        best_score, sort_by, multiple_param, tmp_files_dir)
            
            # GenesAnnotator
            #load_annot = True always
            annotator = self._get_annotator(show_genes)
            
            if show_main:
                datasets_ids = map_config.get_main_datasets()
            
            mapMarkers.enrichment(annotator, show_markers, show_genes, show_anchored, show_how,
                                  datasets_facade, datasets_ids, extend_window, collapsed_view, constrain_fine_mapping = False)
            mapping_results = mapMarkers.get_mapping_results()
            
            sys.stderr.write("Num mapping results:"+str(len(mapping_results.get_mapped()))+"\n")
            
            mapping_results.set_annotator(annotator)
            
            all_mapping_results.append(mapping_results)
            
        return all_mapping_results
   
    ##
    def graph(self, align_form):

        input_file_name = self.__get_input_file(align_form)

        ## Configuration files and paths
        paths_config = self._paths_config
        __app_path = paths_config.get_app_path()

        # Maps
        maps_conf_file = __app_path+MAPS_CONF
        maps_config = MapsConfig(maps_conf_file)
        if align_form.get_maps():
            maps = align_form.get_maps()

            if isinstance(maps, basestring): maps = [maps]

            maps_names = maps_config.get_maps_names(maps)
            maps_ids = maps#maps_config.get_maps_ids(maps_names.strip().split(","))
        else:
            maps_ids = maps_config.get_maps().keys()
            maps_names = ",".join(maps_config.get_maps_names(maps_ids))

        maps_path = paths_config.get_maps_path() #__app_path+config_path_dict["maps_path"]

        ############# ALIGNMENTS - REFERENCES

        # Databases
        databases_conf_file = __app_path+DATABASES_CONF
        databases_config = DatabasesConfig(databases_conf_file, self._verbose)

        alignment_facade = AlignmentFacade(paths_config, verbose = self._verbose)

        ############ Pre-loading of some objects
        ############
        # DatasetsFacade
        # Datasets config
        datasets_conf_file = __app_path+DATASETS_CONF
        datasets_config = DatasetsConfig(datasets_conf_file)
        datasets_ids = datasets_config.get_datasets().keys()

        # Load DatasetsFacade
        datasets_path = paths_config.get_datasets_path() #__app_path+config_path_dict["datasets_path"]
        datasets_facade = DatasetsFacade(datasets_config, datasets_path, maps_path, verbose = self._verbose)

        # Temp directory
        tmp_files_dir = paths_config.get_tmp_files_path()

        ########### Create maps
        ###########
        sort_param = align_form.get_sort()
        multiple_param = True if align_form.get_multiple()=="1" else False
        show_markers = True if align_form.get_show_markers() == "1" else False
        show_genes = True if align_form.get_show_genes() == "1" else False
        show_anchored = True if align_form.get_show_anchored() == "1" else False
        show_main = True if align_form.get_show_main() == "1" else False
        show_how = SHOW_ON_MARKERS if align_form.get_show_how() == "1" else SHOW_ON_INTERVALS
        collapsed_view = align_form.get_collapsed_view()
        constrain_fine_mapping = True
        best_score = True

        aligner = align_form.get_aligner()
        if "," in aligner:
            aligner_list = aligner.strip().split(",")
        else:
            aligner_list = [aligner]

        sys.stderr.write("BMAP aligner_list: "+str(aligner_list)+"\n")

        threshold_id = float(align_form.get_threshold_id())
        threshold_cov = float(align_form.get_threshold_cov())

        all_mapping_results = []
        for map_id in maps_ids:
            sys.stderr.write("bmap_align_graph: Map "+map_id+"\n")

            map_config = maps_config.get_map_config(map_id)
            databases_ids = map_config.get_db_list()

            sort_by = map_config.check_sort_param(map_config, sort_param, self._default_sort)

            if align_form.get_extend() != "":
                if sort_by == MapTypes.MAP_SORT_PARAM_CM:
                    extend_window = float(align_form.get_extend_cm())
                elif sort_by == MapTypes.MAP_SORT_PARAM_BP:
                    extend_window = float(align_form.get_extend_bp())
            else:
                extend_window = 0

            mapMarkers = MapMarkers(maps_path, map_config, alignment_facade, self._verbose)

            mapMarkers.perform_mappings(input_file_name, databases_ids, databases_config, aligner_list,
                                        threshold_id, threshold_cov, self._n_threads,
                                        best_score, sort_by, multiple_param, tmp_files_dir)

            # GenesAnnotator
            #load_annot = True always
            annotator = self._get_annotator(show_genes)

            if show_main:
                datasets_ids = map_config.get_main_datasets()

            mapMarkers.enrichment(annotator, show_markers, show_genes, show_anchored, show_how,
                                  datasets_facade, datasets_ids, extend_window, collapsed_view, constrain_fine_mapping = False)
            mapping_results = mapMarkers.get_mapping_results()

            sys.stderr.write("Num mapping results:"+str(len(mapping_results.get_mapped()))+"\n")

            mapping_results.set_annotator(annotator)

            all_mapping_results.append(mapping_results)

        return all_mapping_results


    ##
    def locate(self, form):
        
        input_file_name = self.__get_input_file(form)
        
        ## Configuration files and paths
        paths_config = self._paths_config
        __app_path = paths_config.get_app_path()
        
        # Maps
        maps_conf_file = __app_path+MAPS_CONF
        maps_config = MapsConfig(maps_conf_file)
        if form.get_maps():
            maps = form.get_maps()
            
            if isinstance(maps, basestring): maps = [maps]
            
            maps_names = maps_config.get_maps_names(maps)
            maps_ids = maps#maps_config.get_maps_ids(maps_names.strip().split(","))
        else:
            maps_ids = maps_config.get_maps().keys()
            maps_names = ",".join(maps_config.get_maps_names(maps_ids))
        
        maps_path = paths_config.get_maps_path() #__app_path+config_path_dict["maps_path"]
        
        ############# ALIGNMENTS - REFERENCES
        
        # Databases
        databases_conf_file = __app_path+DATABASES_CONF
        databases_config = DatabasesConfig(databases_conf_file, self._verbose)
        
        alignment_facade = AlignmentFacade(paths_config, verbose = self._verbose)
        
        ############ Pre-loading of some objects
        ############
        # DatasetsFacade
        # Datasets config
        datasets_conf_file = __app_path+DATASETS_CONF
        datasets_config = DatasetsConfig(datasets_conf_file)
        datasets_ids = datasets_config.get_datasets().keys()
        
        # Load DatasetsFacade
        datasets_path = paths_config.get_datasets_path() #__app_path+config_path_dict["datasets_path"]
        datasets_facade = DatasetsFacade(datasets_config, datasets_path, maps_path, verbose = self._verbose)
        
        # Temp directory
        tmp_files_dir = paths_config.get_tmp_files_path()
        
        ########### Create maps
        ###########
        sort_param = form.get_sort()
        multiple_param = True if form.get_multiple()=="1" else False
        show_markers = True if form.get_show_markers() == "1" else False
        show_genes = True if form.get_show_genes() == "1" else False
        show_anchored = True if form.get_show_anchored() == "1" else False
        show_main = True if form.get_show_main() == "1" else False
        show_how = SHOW_ON_MARKERS if form.get_show_how() == "1" else SHOW_ON_INTERVALS
        collapsed_view = form.get_collapsed_view()
        constrain_fine_mapping = True
        best_score = True
        
        all_mapping_results = []
        for map_id in maps_ids:
            sys.stderr.write("bmap_align: Map "+map_id+"\n")
            
            map_config = maps_config.get_map_config(map_id)
            databases_ids = map_config.get_db_list()
            
            sort_by = map_config.check_sort_param(map_config, sort_param, self._default_sort)
            
            if form.get_extend() != "":
                if sort_by == MapTypes.MAP_SORT_PARAM_CM:
                    extend_window = float(form.get_extend_cm())
                elif sort_by == MapTypes.MAP_SORT_PARAM_BP:
                    extend_window = float(form.get_extend_bp())
            else:
                extend_window = 0
            
            mapMarkers = MapMarkers(maps_path, map_config, alignment_facade, self._verbose)
            
            mapMarkers.locate_positions(input_file_name, sort_by, multiple_param)
            
            # mapMarkers.perform_mappings(input_file_name, databases_ids, databases_config, aligner_list,
            #                             threshold_id, threshold_cov, self._n_threads,
            #                             best_score, sort_by, multiple_param, tmp_files_dir)
            
            # GenesAnnotator
            #load_annot = True always
            annotator = self._get_annotator(show_genes)
            
            if show_main:
                datasets_ids = map_config.get_main_datasets()
            
            mapMarkers.enrichment(annotator, show_markers, show_genes, show_anchored, show_how,
                                  datasets_facade, datasets_ids, extend_window, collapsed_view, constrain_fine_mapping = False)
            mapping_results = mapMarkers.get_mapping_results()
            
            sys.stderr.write("Num mapping results:"+str(len(mapping_results.get_mapped()))+"\n")
            
            mapping_results.set_annotator(annotator)
            
            all_mapping_results.append(mapping_results)
            
        return all_mapping_results
    
    ## Output mapping results
    ##
    def output(self, all_mapping_results, form, html_layout, csv_files):
        
        output_maps = OutputMaps(self._paths_config, self._app_name, html_layout)
        
        output = output_maps.output(all_mapping_results, form, csv_files)
        
        return output
    
    ## Obtain csv files
    ##
    def csv_files(self, all_mapping_results, form):
        
        csv_writer = CSVWriter(self._paths_config, self._verbose)
        
        csv_files = csv_writer.output_maps(all_mapping_results, form)
        
        return csv_files
    
    ## Send email with results
    ##
    def email(self, form, csv_files, email_conf):
        
        # Maps configuration files
        paths_config = self._paths_config
        __app_path = paths_config.get_app_path()
        maps_conf_file = __app_path+MAPS_CONF
        maps_config = MapsConfig(maps_conf_file, self._verbose)
        
        try:
            csv_filenames = []
            csv_filedescs = []
            maps_csv_files = csv_files.get_maps_csv_files()
            for map_id in maps_csv_files:
                map_name = maps_config.get_map_config(map_id).get_name()
                
                map_csv_files = maps_csv_files[map_id]
                if map_csv_files.get_mapped():
                    csv_filenames.append(map_csv_files.get_mapped())
                    csv_filedescs.append(map_name+".mapped")
                
                if map_csv_files.get_map_with_genes():
                    csv_filenames.append(map_csv_files.get_map_with_genes())
                    csv_filedescs.append(map_name+".with_genes")
                
                if map_csv_files.get_map_with_markers():
                    csv_filenames.append(map_csv_files.get_map_with_markers())
                    csv_filedescs.append(map_name+".with_markers")
                
                if map_csv_files.get_map_with_anchored():
                    csv_filenames.append(map_csv_files.get_map_with_anchored())
                    csv_filedescs.append(map_name+".with_anchored")
                
                if map_csv_files.get_unmapped():
                    csv_filenames.append(map_csv_files.get_unmapped())
                    csv_filedescs.append(map_name+".unmapped")
                
                if map_csv_files.get_unaligned():
                    csv_filenames.append(map_csv_files.get_unaligned())
                    csv_filedescs.append(map_name+".unaligned")
                
            
            ## Send CSV by EMAIL if requested
            if form.get_send_email() and form.get_send_email()=="1" and len(csv_filenames)>0:
                m2p_mail.send_files(form, csv_filenames, csv_filedescs, email_conf)
            
        except m2pException as e:
            ## Just log it, but keep giving output maps to the user
            sys.stderr.write("Error sending email.\n")
        
        return

## END
