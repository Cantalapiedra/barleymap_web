#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlLayoutBarleymap.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

class HtmlLayoutBarleymap(object):
    
    @staticmethod
    def output_html_img_button(action, url, img_url, width = "3%", height = "3%", img_url_hover = None):
        output = []
        if url and img_url:
            output.append("""<a href="{1}">
                          <img style="width:{2};height:{3}; border:0;"
                          onmouseover="hover_{0}(this);" onmouseout="unhover_{0}(this);"
                          src="{4}"/>
                          </a>""".format(action, url, width, height, img_url))
            
            if img_url_hover:
                # Functions to change maps image (zoom or full maps)
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
                """.format(action, img_url, img_url_hover))
        else:
            Exception("HtmlLayoutBarleymap: No URL or img_url provided for img button.")
        
        return "".join(output)
    
    @staticmethod
    def main_text(citation, base_url, PREFIX_UI_CTRLS_ALIGN, PREFIX_UI_CTRLS_FIND, PREFIX_UI_CTRLS_LOCATE):
        output = []
        #output.append('<br/>')
        output.append('<div id="main_buttons" style="margin:0px;">')
        output.append('<table id="main_buttons_table" center><tr>')
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button(PREFIX_UI_CTRLS_FIND, base_url+"/"+PREFIX_UI_CTRLS_FIND+"/",
                                                                 base_url+"/img/ui_buttons_find.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_find_hover.png"))
        output.append("</td>")
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button(PREFIX_UI_CTRLS_ALIGN, base_url+"/"+PREFIX_UI_CTRLS_ALIGN+"/",
                                                                 base_url+"/img/ui_buttons_align.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_align_hover.png"))
        output.append("</td>")
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button(PREFIX_UI_CTRLS_LOCATE, base_url+"/"+PREFIX_UI_CTRLS_LOCATE+"/",
                                                                 base_url+"/img/ui_buttons_locate.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_locate_hover.png"))
        output.append("</td>")
        output.append('<td style="text-align:center;">')
        output.append(HtmlLayoutBarleymap.output_html_img_button("help", base_url+"/help/",
                                                                 base_url+"/img/ui_buttons_help.png", "200px", "100px",
                                                                 base_url+"/img/ui_buttons_help_hover.png"))
        output.append("</td>")
        output.append("</tr>")
        output.append("</table>")
        output.append("</div>")
        #output.append('<br/>')
        
        output.append('<div id="main_text">')
        output.append(HtmlLayoutBarleymap.text_menu(citation, base_url, show_last_changes = True))
        output.append("</div>")
        
        return "".join(output)
    
    @staticmethod
    def head(base_url):
        return """
        <!DOCTYPE html>
        <!--[if lt IE 7 ]> <html class="ie6"> <![endif]-->
        <!--[if IE 7 ]>    <html class="ie7"> <![endif]-->
        <!--[if IE 8 ]>    <html class="ie8"> <![endif]-->
        <!--[if IE 9 ]>    <html class="ie9"> <![endif]-->
        <!--[if (gt IE 9)|!(IE)]><!--> <html class=""> <!--<![endif]-->
        <head>
            <meta charset="utf-8" />
            <title>Barleymap</title>
            <meta content="CPCantalapiedra" name="CPCantalapiedra" />
            <meta content="Map markers to the barley genome" name="Map markers to the barley genome" />
            <meta content="barley, barleymap, physical map, genetic map, markers, mapping, bioinformatics, blast, gmap, genome, genomics" name="keywords" />
            <link rel="stylesheet" href="{0}" type="text/css" media="screen"/>
        </head>""".format(base_url+"/style.css")
    
    @staticmethod
    def js_scripts(base_url, app_google_analytics_id):
        scripts = ""
        
        scripts = """
            <body>
        <script src="{0}"></script>
        <script src="{1}"></script>
        """.format("https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js", \
                   base_url+"/js/index.js")
        
        scripts = scripts + """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id="""+app_google_analytics_id+""""></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', '"""+app_google_analytics_id+"""');
        </script>
        """
        
        return scripts
    
    @staticmethod
    def js_scripts_maps(base_url, app_google_analytics_id):
        scripts = ""
        
        scripts = """
            <body>
        <script src="{0}"></script>
        <script src="{1}"></script>
        """.format("http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js", \
                   base_url+"/js/maps.js")
        
        scripts = scripts + """
        <!-- Google Analytics -->
        <script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
            })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
          
            ga('create', '"""+app_google_analytics_id+"""', 'auto');
            ga('send', 'pageview');
          
        </script>
        """
        
        return scripts
    
    @staticmethod
    def title_header(base_url):
        return """
        <header id="top">
            <h2><a href="{1}/">Barleymap</a></h2>
            <h3 class="infobar">({0})</h3>
        </header>
        """.format("Map markers to the barley genome - MorexV3 2021 edition", base_url)
    
    @staticmethod
    def footer():
        return """
        <footer class="infobar">
            <a href="http://www.eead.csic.es/compbio/" target="_blank">Computational and structural biology group</a>
            ::
            <a href="http://eead.csic.es/" target="_blank">Estaci&oacute;n Experimental de Aula Dei</a>
            ::
            <a href="http://www.csic.es/" target="_blank">Consejo Superior de Investigaciones Cient&iacute;ficas</a>
        </footer>
        """
    
    @staticmethod
    def text_menu(citation, base_url, show_last_changes = False):
        text_buffer = []
        if show_last_changes:
            text_buffer.append("""
            <br/><strong>Latest changes</strong>
            <br/>08-02-2024:<br/>
            . Check out barley pangenes and their conservation at <a href="https://eead-csic-compbio.github.io/barley_pangenes">https://eead-csic-compbio.github.io/barley_pangenes/</a>.
            <br/>
            <br/>22-08-2023:<br/>
            . Results can now be correctly exported as CSV files after fixing bug.
            <br/>
            <br/>19-06-2023:<br/>
            . Mapped DartSeq markers on MorexV3 by user request.
            <br/>
            <br/>15-03-2023:<br/>
            . Moved to new server and updated URL (<a href="https://barleymap.eead.csic.es">https://barleymap.eead.csic.es</a>).
            <br/>
            <br/>14-06-2022:<br/>
            . Added lifted-over IBSC 2012 & 2016 gene models to MorexV3 map.
            <br/>
            <br/>04-11-2021:<br/>
            · Added MorexV3 map + centromeres, PGSB and BaRT1.0 gene models and NCBI Entrez CDS sequeces (see release <a href='https://bioinfoperl.blogspot.com/2021/11/barleymapmorexv3release.html'>notes</a>).
            <br/>
            <br/>17-08-2018:<br/>
            · Added POPSEQ map updated with 2017 data<sup>[3]</sup> (POPSEQ_2017).
            <br/>
            <br/>6-03-2018:<br/>
            · Added a dataset of NCBI genes to the Morex Genome map. This dataset includes genes like HvCO1, Int-c, Btr1, Vrs1, PhyB, HvCEN, etc... to a total of 894 entries.
            <br/>
            <br/>19-12-2017:<br/>
            · Support for the <strong>Illumina50K</strong><sup>[4]</sup> markers, which can now be searched in the
            IBSC<sup>[1]</sup>, POPSEQ<sup>[2]</sup> and Morex Genome<sup>[3]</sup> released in 2017,
            through the
            <strong><i><a href="{0}/find/">Find markers</a></i></strong> option.
            <br/>
        """.format(base_url))
            
        text_buffer.append("""
            <br/><br/>
            <hr/>
            <b><a href="{2}">Barleymap</a></b> was designed to search the position of barley genetic markers
            on the <strong>Barley Physical Map</strong> (IBSC<sup>[1]</sup>) 
            ,the <strong>POPSEQ map</strong> (Mascher <i>et al.</i><sup>[2]</sup>) and the 
            2017 Morex Genome. 
            The current version was updated to work with the <strong>MorexV3</strong> genome (released in 2021)<sup>[5]</sup>.
            <br/><br/>
            
            All the public data used by Barleymap can be found at
            <a href="https://www.helmholtz-muenchen.de/pgsb/index.html" target="_blank">PGSB</a>
            , <a href="https://galaxy-web.ipk-gatersleben.de/" target="_blank">IPK</a> 
            , <a href="http://doi.org/10.5447/ipk/2021/3" target="_blank">e!DAL</a>
            , <a href="https://ics.hutton.ac.uk/barleyrtd" target="_blank">Barley RTD</a>
            and the <a href="https://www.ncbi.nlm.nih.gov/assembly/GCA_904849725.1" target="_blank">NCBI</a>.
            <br/><br/>
            
            The <strong><i><a href="{2}/find/">Find markers</a></i></strong> option allows to find the position of markers by using their identifiers as input.
            <br/>Note that those markers must be part of one of the
            <!--<strong><a href="{0}#barleymap_datasets">-->precalculated datasets<!--</a></strong>--> available (e.g.: Illumina 50K markers).
            <br/><br/>
            
            To use the <strong><i><a href="{2}/align/">Align sequences</a></i></strong> option you must provide nucleotide sequences of the markers (in FASTA format).
            <br/>These will be used to retrieve their positions through
            <strong><a href="{0}#references_and_algorithms_used_for_alignment">sequence alignment</a></strong> to the selected map (IBSC2012, POPSEQ, MorexGenome or MorexV3).
            <br/><br/>
            
            The <strong><i><a href="{2}/locate/">Locate by position</a></i></strong> option allows to examine the map context of specific positions,
            which must be provided as tuples with chromosome (or contig) and position (local position, within the chromosome or contig, in base pairs).
            For example, an user could provide as input "chr1H   10000" to find out which genes are in that specific region of chromosome 1H.
            <br/><br/>
            
            In addition to locate a list of markers or sequences,
            <strong><a href="{0}#genes_markers_enrichment_and_annotation">information of genes, genetic markers, and anchored features,</a></strong>
            that enrich the context around or between the queries will be shown.<br/><br/>
            
            <strong><a href="https://github.com/Cantalapiedra/barleymap_web">Barleymap web</a></strong> 
            works on top of <strong><a href="https://github.com/Cantalapiedra/barleymapcore">barleymap core API</a></strong>, used also in a
            <strong><a href="https://github.com/Cantalapiedra/barleymap">standalone application</a></strong>
            that allows loading custom databases, maps and datasets, among other features.
            <br/>Such application can be used with data from any organism for which sequences anchored to a genetic/physical background are available.
            
            <br/><br/>
            
            <strong>Further information</strong> about how this tool works and help on using it can be found
            <strong><a href="{0}">here</a></strong>.
            <br/>
            Or you may wish to <strong>contact</strong> the <a href="http://www.eead.csic.es/compbio/" target="_blank">Computational and structural biology group</a>
            (<a href="http://www.eead.csic.es">EEAD</a> - <a href="http://www.csic.es">CSIC</a>):<br/>
            <a href="mailto:cpcantalapiedra@gmail.com">Carlos P Cantalapiedra</a>
            <br/>
            <a href="mailto:bcontreras@eead.csic.es">Bruno Contreras-Moreira</a>
            <br/><br/>
            
            <strong>Citation:</strong>
            <a href="http://link.springer.com/article/10.1007%2Fs11032-015-0253-1">{1}</a>
            <br/><br/>
            <hr/>
            <br/>
            
            <cite><sup>[1]</sup>IBSC. 2012.
            <a href="http://dx.doi.org/10.1038/nature11543" target="_blank">
            A physical, genetic and functional sequence assembly of the barley genome.
            </a>
            Nature. 491:711-16. doi:10.1038/nature11543
            </cite>
            <br/>
            
            <cite><sup>[2]</sup>Mascher et al. 2013.
            <a href="http://onlinelibrary.wiley.com/doi/10.1111/tpj.12319/abstract" target="_blank">
            Anchoring and ordering NGS contig assemblies by population sequencing (POPSEQ).
            </a>
            The Plant Journal, 76: 718-27. doi:10.1111/tpj.12319
            </cite>
            <br/>
            
            <cite><sup>[3]</sup>Mascher et al. 2017
            <a href="https://www.nature.com/articles/nature22043" target="_blank">
            A chromosome conformation capture ordered sequence of the barley genome
            </a>
            Nature. 544:427-433. doi:10.1038/nature22043
            </cite>
            <br/>
            
            <cite><sup>[4]</sup>Bayer et al. 2017
            <a href="https://www.frontiersin.org/articles/10.3389/fpls.2017.01792/full" target="_blank">
            Development and Evaluation of a Barley 50k iSelect SNP Array
            </a>
            Frontiers in Plant Science. 8:1792. doi:10.3389/fpls.2017.01792
            </cite>
            </br>
            
            <cite><sup>[5]</sup>Mascher et al. 2021
            <a href="https://doi.org/10.1093/plcell/koab077" target="_blank">
            Long-read sequence assembly: a technical evaluation in barley
            </a>
            The Plant Cell 33(6):1888–1906 doi:10.1093/plcell/koab077
            </cite>
            </br>

            <cite><sup>[6]</sup>Rapazote-Flores et al. 2019
            <a href="https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-6243-7" target="_blank">
            BaRTv1.0: an improved barley reference transcript dataset to determine accurate changes in the barley transcriptome using RNA-seq
            </a>
            BMC Genomics 20:968 doi:10.1186/s12864-019-6243-7
            </cite>


        """.format(base_url+"/help/", citation, base_url))
        
        return "".join(text_buffer)
    
## END
