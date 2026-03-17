#!/usr/bin/env python
# -*- coding: utf-8 -*-

# map_svg_img.py is part of Barleymap web app.
# Copyright (C)  2013-2014  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys
from subprocess import Popen, PIPE

from barleymapcore.m2p_exception import m2pException

## OUTPUT GENETIC MAP
def output_genetic_map(map_csv_file, genmap_path, map_chrom_order_file, map_as_physical, fine_mapping = False, pos_position = 2):
    
    ## NOTE: chr_list it was intended to obtain a different output for every chromosome
    ## but it is not being used actually
    
    sys.stderr.write("map_svg_img.py: Creating svg file...\n")
    
    if not map_csv_file or map_csv_file.strip() == "": raise m2pException("No CSV file to create image map.")
    
    svg_code = []
    try:
        command_params = [genmap_path+"genmap.pl", "--map="+map_csv_file, "--chrom-order="+map_chrom_order_file]
        
        if map_as_physical: command_params.append("--map_as_physical")
        if fine_mapping: command_params.append("--fine_mapping")
        # Using the same value for position on mapping results and for position on chrom config file
        # If could be a different one, but with morexgenome, ibsc and popseq they are the same
        command_params.append("--pos_position="+str(pos_position))
        command_params.append("--chrommax="+str(pos_position))
        command_params.append(" | grep -v \"<?xml\" | grep -v \"<!DOCTYPE\"")
        
        command = " ".join(command_params)
        
        retValue = 0
        #FNULL = open(os.devnull, 'w')
        #if verbose:
        #    p = Popen(gmap_cmd, shell=True, stdout=PIPE, stderr=sys.stderr)
        #else:
        p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        
        #p = Popen(command, shell=True, stdout=PIPE, stderr=sys.stderr)
        com_list = p.communicate()
        output = com_list[0]
        output_err = com_list[1]
        retValue = p.returncode
        
        if retValue != 0:
            raise Exception("map_svg_img: genmap.pl return != 0. "+command+"\n"+str(output_err)+"\n")
        
        # Clean SVG code to embbed it in html5
        [svg_code.append(line) for line in output.strip().split("\n") if (line != "")]# and not line.startswith("#") and not line.startswith(">"))]
        
        #sys.stderr.write("".join(svg_code)+"\n")
        #sys.stderr.write(str(output_err)+"\n")
        
    except Exception:
        raise
    finally:
        pass
    
    sys.stderr.write("map_svg_img.py: svg file created.\n")
    
    return "".join(svg_code)

## END