#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsAlign.py is part of Barleymap web app.
# Copyright (C) 2017 Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

from HtmlComponentsBase import HtmlComponentsBase

class HtmlComponentsAlign(object):
    
    ################################## ALIGN HTML COMPONENTS
    ########################################################
    @staticmethod
    def align(base_url, align_form, PREFIX_UI_CTRLS_ALIGN, maps_config):
        output = []
        
        ####### INPUT QUERY TEXT AREA
        output.append("""
        <section id="content">
            <form name="input_align" action="{0}" method="post" enctype="multipart/form-data">
            """.format(base_url+"/mapmarkers/align"))
        
        output.append(HtmlComponentsBase._load_query_area_align(align_form.get_query(),
                                                align_form.get_user_file(),
                                              "Input FASTA sequences (1-word header):",
                                              PREFIX_UI_CTRLS_ALIGN))
        output.append("<br/>")
        output.append("<table><tr><td>")
        output.append(HtmlComponentsBase._load_output_area(align_form.get_multiple(),
                                         align_form.get_sort(),
                                         align_form.get_send_email(),
                                         align_form.get_email_to(),
                                         PREFIX_UI_CTRLS_ALIGN))
        output.append("</td><td>")
        output.append(HtmlComponentsBase._load_genes_area(align_form.get_show_markers(),
                                        align_form.get_show_genes(),
                                        align_form.get_show_anchored(),
                                        align_form.get_show_main(),
                                        align_form.get_show_how(),
                                        align_form.get_extend(),
                                        align_form.get_extend_cm(),
                                        align_form.get_extend_bp(),
                                        PREFIX_UI_CTRLS_ALIGN))
        
        output.append("</td></tr></table>")
        output.append("<br/>")
        
        output.append(HtmlComponentsBase._load_alignment_area(align_form.get_aligner(),
                                            align_form.get_threshold_id(),
                                            align_form.get_threshold_cov()))
        output.append("<br/>")
        
        output.append("""
                <table><tr>
                <td>
                    <fieldset id="align_fieldset" style="border:solid thin;">
                    <legend style="text-align:left;">Choose map:</legend>
                    """)
        
        #### MAPS
        output.append(HtmlComponentsBase._load_data(align_form.get_maps(), maps_config.get_maps_tuples(), "maps"))
        
        output.append("""
                      
                    </fieldset>
                </td><td id="submit_button_td">
                    <button id="submit_button" name="action" type="submit" value="Blast">
                        <img src="{0}" onmouseover="hover_{1}(this);" onmouseout="unhover_{1}(this);"/>
                    </button>
                </td>
                </tr></table>
            </form>
        </section><hr/> <!-- content -->
        """.format(base_url+"/img/ui_buttons_align.png", "align"))
        
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
        """.format("align", base_url+"/img/ui_buttons_align_mini.png", base_url+"/img/ui_buttons_align_mini_hover.png"))
        
        return "".join(output)
    
## END
