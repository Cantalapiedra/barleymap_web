#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsLocate.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys

from HtmlComponentsBase import HtmlComponentsBase

class HtmlComponentsLocate(object):
    
    ######################### LOCATE FORM HTML COMPONENTS
    ###################################################
    @staticmethod
    def locate(base_url, form, PREFIX_UI_CTRLS_LOCATE, maps_config):
        output = []
        
        ####### INPUT QUERY TEXT AREA
        output.append("""
        <section id="content">
            <form name="input_locate" action="{0}" method="post" enctype="multipart/form-data">
            """.format(base_url+"/mapmarkers/locate"))
        
        output.append(HtmlComponentsBase._load_query_area_locate(form.get_query(),
                                            form.get_user_file(),
                                             "Input a list of positions:",
                                             PREFIX_UI_CTRLS_LOCATE))
        output.append("<br/>")
        output.append("<table><tr><td>")
        output.append(HtmlComponentsBase._load_output_area(form.get_multiple(),
                                         form.get_sort(),
                                         form.get_send_email(),
                                         form.get_email_to(),
                                         PREFIX_UI_CTRLS_LOCATE))
        output.append("</td><td>")
        output.append(HtmlComponentsBase._load_genes_area(form.get_show_markers(),
                                        form.get_show_genes(),
                                        form.get_show_anchored(),
                                        form.get_show_main(),
                                        form.get_show_how(),
                                        form.get_extend(),
                                        form.get_extend_cm(),
                                        form.get_extend_bp(),
                                        PREFIX_UI_CTRLS_LOCATE))
        output.append("</td></tr></table>")
        output.append("<br/>")
        
        output.append("""
                <table><tr>
                <td>
                    <fieldset id="locate_fieldset" style="border:solid thin;">
                    <legend style="text-align:left;">Choose map:</legend>
                    """)
        
        #### MAPS
        output.append(HtmlComponentsBase._load_data(form.get_maps(), maps_config.get_maps_tuples(), "maps"))
        
        output.append("""
                      
                    </fieldset>
                </td><td id="submit_button_td">
                    <button class="boton" id="submit_button" name="action" type="submit" value="Locate">
                        <img src="{0}" onmouseover="hover_{1}(this);" onmouseout="unhover_{1}(this);"/>
                    </button>
                </td>
                </tr></table>
            </form>
        </section><hr/> <!-- content -->
        """.format(base_url+"/img/ui_buttons_locate.png", "locate"))
        
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
        """.format("locate", base_url+"/img/ui_buttons_locate_mini.png", base_url+"/img/ui_buttons_locate_mini_hover.png"))
        
        return "".join(output)

## END
