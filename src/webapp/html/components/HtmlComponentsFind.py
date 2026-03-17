#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsFind.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys

from HtmlComponentsBase import HtmlComponentsBase

class HtmlComponentsFind(object):
    
    ######################### FIND FORM HTML COMPONENTS
    ###################################################
    @staticmethod
    def find(base_url, find_form, PREFIX_UI_CTRLS_FIND, maps_config):
        output = []
        
        ####### INPUT QUERY TEXT AREA
        output.append("""
        <section id="content">
            <form name="input_find" action="{0}" method="post" enctype="multipart/form-data">
            """.format(base_url+"/mapmarkers/find"))
        
        output.append(HtmlComponentsBase._load_query_area_find(find_form.get_query(),
                                            find_form.get_user_file(),
                                             "Input a list of marker IDs:",
                                             PREFIX_UI_CTRLS_FIND))
        output.append("<br/>")
        output.append("<table><tr><td>")
        output.append(HtmlComponentsBase._load_output_area(find_form.get_multiple(),
                                         find_form.get_sort(),
                                         find_form.get_send_email(),
                                         find_form.get_email_to(),
                                         PREFIX_UI_CTRLS_FIND))
        output.append("</td><td>")
        output.append(HtmlComponentsBase._load_genes_area(find_form.get_show_markers(),
                                        find_form.get_show_genes(),
                                        find_form.get_show_anchored(),
                                        find_form.get_show_main(),
                                        find_form.get_show_how(),
                                        find_form.get_extend(),
                                        find_form.get_extend_cm(),
                                        find_form.get_extend_bp(),
                                        PREFIX_UI_CTRLS_FIND))
        output.append("</td></tr></table>")
        output.append("<br/>")
        
        output.append("""
                <table><tr>
                <td>
                    <fieldset id="find_fieldset" style="border:solid thin;">
                    <legend style="text-align:left;">Choose map:</legend>
                    """)
        
        #### MAPS
        output.append(HtmlComponentsBase._load_data(find_form.get_maps(), maps_config.get_maps_tuples(), "maps"))
        
        output.append("""
                      
                    </fieldset>
                </td><td id="submit_button_td">
                    <button class="boton" id="submit_button" name="action" type="submit" value="Find">
                        <img src="{0}" onmouseover="hover_{1}(this);" onmouseout="unhover_{1}(this);"/>
                    </button>
                </td>
                </tr></table>
            </form>
        </section><hr/> <!-- content -->
        """.format(base_url+"/img/ui_buttons_find.png", "find"))
        
        output.append("""
        <script>
            // Functions to change image with mouse over and out
            function hover_{0}(element) {{
                element.setAttribute('src', '{2}');
            }}
            function unhover_{0}(element) {{
                element.setAttribute('src', '{1}');
            }}
        </script>
        """.format("find", base_url+"/img/ui_buttons_find_mini.png", base_url+"/img/ui_buttons_find_mini_hover.png"))
        
        return "".join(output)

## END