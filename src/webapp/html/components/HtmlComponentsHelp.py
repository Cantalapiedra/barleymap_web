#!/usr/bin/env python
# -*- coding: utf-8 -*-

# HtmlComponentsHelp.py is part of Barleymap web app.
# Copyright (C) 2017-2023 Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

class HtmlComponentsHelp(object):
    
    @staticmethod
    def _help_menu(output_buffer):
        output_buffer.append("""
            <article class="help_article">
                <section class="help_section">
                    <hr/>
                    <ul class="help_menu">
                        <li><a href="#overview">
                        
                            Overview
                            
                        </a></li>
                        <li><a href="#find_markers">
                        
                            Find markers
                            
                        </a></li>
                            <ul>
                                <li><a href="#datasets_included">
                                
                                    Datasets included in Barleymap web
                                    
                                </a></li>
                            </ul>
                            
                        <li><a href="#align_sequences">
                        
                            Align sequences
                            
                        </a></li>
                            <ul>
                                <li><a href="#references_included">
                                
                                    References included in Barleymap web
                                    
                                </a></li>
                            </ul>
                        <li><a href="#locate_by_position">
                        
                            Locate by position
                            
                        </a></li>
                        
                        <li><a href="#barleymap_output">
                        
                            Barleymap output
                            
                        </a></li>
                            
                        <li><a href="#confidentiality">
                        
                            Confidentiality
                            
                        </a></li>
                        
                        <li><a href="#disclaimer">
                        
                            Disclaimer
                            
                        </a></li>
                        
                        <li><a href="#references">
                        
                            References
                            
                        </a></li>
                    </ul>
                """)
        
        return
    
    @staticmethod
    def help(base_url):
        output_buffer = []
        output_buffer.append("""
                             <section id="content">
                                <a href="{0}"><img style="width:5%;height:5%;border:none;" src="{1}" alt="back"/></a>
                             """.format(base_url+"/", base_url+"/img/back.gif"))
        
        output_buffer.append("""<br/>""")
        
        HtmlComponentsHelp._help_menu(output_buffer)
        
        ## OVERVIEW
        
        output_buffer.append("""
                    <hr/>
                    
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="overview">Overview</h2>
                    
                        <br/>
                        Barleymap was designed to search the genetic and physical positions of barley markers on
                        the <strong>Barley Physical Map</strong> (IBSC<sup>[1]</sup>) and
                        the <strong>POPSEQ</strong> map<sup>[2]</sup>. The strong>Morex Genome</strong><sup>[3]</sup> map
                        was subsequently added in 2017. The current version uses the <strong>MorexV3</strong> genome<sup>[5]</sup> by default.
                        <br/><br/>
                        Barleymap provides <strong>three tools</strong> to retrieve data from the maps:
                        <ul class="help_list">
                            <li>"Find markers": to retrieve the position of markers providing their identifiers.</li>
                            <li>"Align sequences": to obtain the position of FASTA sequences by pairwise alignment.</li>
                            <li>"Locate by position": to examine specific loci by map position.</li>
                        </ul>
                        <br/>
                """.format(base_url))
        
        ## FIND MARKERS
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="find_markers">Find markers</h2>
                        
                        <br/>
                        
                        The "Find markers" tool allows searching for loci which are commonly used by the barley community.
                        These loci include genetic markers, genes, BAC contigs, WGS contigs, etc. from different <strong>datasets</strong>.
                        Their map positions have been previously computed and stored, so that the users can retrieve
                        them by providing the identifier of the locus.
                        
                        <br/><br/>
                        
                        Be aware that "Find markers" datasets were generated using <strong>fixed parameters</strong>.
                        In those cases when the user wants to perform a more specific search, 
                        e.g. by choosing the alignment tool or parameters, 
                        it is recommended to get the FASTA sequence of the query and use the "Align sequences" tool instead.
                        
                        <br/><br/>
                        
                        As <strong>input data</strong>, the user must provide a list of identifiers to use as queries. Besides that,
                        the user needs to choose which is the <strong>map</strong> (or maps) from which to obtain the positions,
                        using the selection list "Choose maps".
                        
                        <br/><br/>
                        
                        The "Genes/Markers enrichment" area allows the user to customize which <strong>additional data</strong> will be output along
                        with the map positions of queries. First, the user can choose whether to show "genes", "markers" and/or "anchored".
                        The last usually refers to WGS contigs, BAC contigs, or other elements associated to map positions (anchored), 
                        but which lack a biological meaning per se.
                        Besides that, the user can also choose whether to "show only main features" for each map.
                        For example, for Morex Genome, "HORVU" genes are configured as "main" whereas "MLOCs" are not.
                        The "Add features" option involves 2 ways to add additional data to the results:
                        
                        <ul class="help_list">
                            <li>
                            "on markers": the additional data is searched for each marker independently.
                            Each additional row is appended after the query position.
                            </li>
                            
                            <li>
                            "on intervals": the additional data is searched in the regions defined by all the queries.
                            Each additional row is added only once, and in its actual position in relation to the queries.
                            </li>
                        </ul>
                        
                        Therefore, the "on markers" option is better to obtain detailed data associated to each query,
                        whereas the "on intervals" option is better to obtain a map-like result.
                        Note that both previous options show additional data in the same position as queries by default.
                        To obtain additional data around the markers the "Extend genes/markers search" option
                        must be activated and the interval, in cM or bp, depending on the value of the "Sort by" option (see below), should be adjusted.
                        
                        <br/><br/>
                        
                        <strong>Other parameters</strong> include whether to show or not markers with multiple mappings,
                        whether to sort the output by centimorgans (cM) or basepairs (bp), and an option to send the results to an email address provided by the user.
                        Note that the option "Sort by" will be applied only for IBSC2012, which has both cM and bp positions available.
                        POPSEQ data will be always sorted by cM, and Morex Genome data by bp.
                        
                        <br/><br/>
                        
                        <h3 id="datasets_included">Datasets included in Barleymap web</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        <br/>
                        
                        The next is a list of datasets whose map positions have been pre-computed and stored in this instance of the Barleymap web application.
                        Note that the
                        <a href="https://github.com/Cantalapiedra/barleymap">standalone version</a> or a custom
                        <a href="https://github.com/Cantalapiedra/barleymap_web">web version</a> of barleymap could be used to create other datasets.
                        
                        <ul class="help_list">
                        
                            <li>
                                <b>BOPA1</b> dataset<sup>[4][11]</sup>: bears 1,536 sequences.
                                "BOPA consensus" (e.g.: 11_20003) or
                                "POPA12" identifiers must be provided (e.g.: ABC09016-2-2-348, 7174-365, BOPA1_7174-365, ...).
                                <br/>
                                A full list of markers, different identifiers and their sequences can be found at [4][11] (supplementary Table S9).
                            </li>
                            
                            <li>
                                <b>BOPA2</b> dataset<sup>[4][11]</sup>: bears 1,536 sequences.
                                "BOPA consensus" identifiers must be provided (e.g.: 12_31342, i_12_31342, BOPA2_12_31342).
                                <br/>
                                A full list of markers, different identifiers and their sequences can be found at [4][11] (supplementary Table S10; "POPA" identifiers are also used often, see Table S14). 
                            </li>
                            
                            <li>
                                <b>Illumina iSelect Infinium</b><sup>[5]</sup>: 7,864 sequences.
                                Identifiers can be provided in different formats (e.g.: i_11_10882, 11_10882, 6964-414, BOPA1_6964-414, ...).
                                <br/>
                                A full list of markers, different identifiers and their sequences can be found at [5] (supplementary Table 6).
                                <br/>
                                (Illumina Infinium iSelect technology belongs to Illumina®)
                            </li>
                            
                            <li>
                                <b>Illumina 50K</b><sup>[6][*]</sup>: 43,078 sequences with positions provided by JHI. Morex Genome and MorexV3 only.
                                "Illumina 50K" identifiers must be provided (e.g.: JHI-Hv50k-2016-7), but it accepts previous identifiers for
                                markers from previous datasets (e.g. SCRI_RS_10006).
                                <br/>
                                A full list of markers, different identifiers and their sequences can be found at [6][*'] (supplementary Table XX).
                                <br/>
                                (Illumina Infinium technology belongs to Illumina®)
                            </li>
                            
                            <li><b>DArTs</b><sup>[7][6]</sup>: 2,000 sequences (e.g.: bPb-3150 or bPb-3150_PUR_f+r, bPb-2614 or bPb-2614_WSU_r).
                                <br/>Sequences for DArTs can be found at [7][6'].
                            </li>
                            
                            <li><b>DArTseq SNPs</b><sup>[8][7]</sup>: 8,535 sequences (e.g.: 3254894|F|0 or 3254894).</li>
                            
                            <li><b>DArTseq PAVs (SilicoDArTs)</b><sup>[8][7]</sup>: 15,526 sequences (e.g.: 3271396|F|0 or 3271396).
                                <br/>
                                NOTE that 1,761 sequences from DArTseq are PAVs and contain SNPs, so that the identifier is the same for both markers.
                                <br/>
                                (DArTs<sup>TM</sup> and DArTseq<sup>TM</sup> technologies belong to Diversity Arrays Technology®)
                            </li>
                            
                            <li><b>Oregon Wolfe Barley GBS SNPs</b><sup>[9][8]</sup>: 34,396 sequences (e.g.: owbGBS1162 or owbGBS34926).
                                <br/>
                                A full list of markers their sequences can be found at [9][8] (supplementary Dataset S1).
                            </li>
                            
                            <li><b>Haruna nijo cultivar flcDNAs</b><sup>[10][9]</sup>: 28620 sequences (e.g.: AK358336 or AK358336.1).</li>
                            
                            <li><b>HarvEST Unigenes (assembly #36)</b><sup>[11][10]</sup>: 70148 sequences (e.g.: U36_70143 or U36_998).</li>
                            
                            <li><b>IBSC2012 genes</b><sup>[2][*]</sup>: 14,923 HC and 19,415 LC genes (e.g.: MLOC_67805).</li>
                            
                            <li><b>IBSC2012 BES</b><sup>[2][*]</sup>: IBSC_2012 and Morex Genome only. More than 400,000 BAC-End sequences
                            (e.g.: HV_MBa0001A01.f.scf).</li>
                            
                            <li><b>IBSC2012 BAC contigs</b><sup>[2][*]</sup>: IBSC_2012 only. 377,144 BAC contigs. 
                            (e.g. HVVMRX83KHA0104A24_HVVMRXALLhA0391C07_v16_c28)</li>
                            
                            <li><b>IBSC2012 WGS contigs (Morex, Barke and Bowman)</b><sup>[2][*]</sup>:
                            Barke and Bowman contigs mapped in IBSC_2012 and Morex Genome only.
                            Morex contigs in POPSEQ map also.
                           (e.g. morex_contig_15371, barke_contig_975766, bowman_contig_387623).</li>
                            
                            <li><b>NCBI barley genes</b><sup>[11][*]</sup>: Morex Genome only.
                            894 sequences (e.g.: AAD02252.1, dhn11, AAF01699.1).</li>
                            
                            <li><b>IBSC2016 genes</b><sup>[3][*]</sup>: Morex Genome only.
                            39,734 HC and 41,949 LC genes.
                            (e.g.: HORVU1Hr1G000090).</li>
                            
                            <li><b>PGSB genes</b><sup>[14]</sup>: MorexV3 only.
                            35,826 HC and 45,849 LC genes.
                            (e.g.: HORVU.MOREX.r3.1HG0000030).</li>
                            
                            <li><b>BaRT 1.0 gene models</b><sup>[15]</sup>: MorexV3 only.
                            45,619 genes.
                            (e.g.: BART1_0-u00002).</li>

                            <li><b>BaRT 2.18 transcript isoforms</b><sup>[15]</sup>: MorexV3 only.
                            133647 transcripts.
                            (e.g.: BaRT2v18chr1HG000020.1).</li>            

                            <li><b>panBaRT20 transcript isoforms</b><sup>[16]</sup>: MorexV3 only.
                            565817 transcripts.
                            (e.g.: PanBaRT20_chr1HG00001.1).</li>

                            <li><b>Entrez CDS</b>: MorexV3 only.
                            292 sequences (e.g.: BAO51910.1, LEA3).</li>						 

                            <li><b>centromers</b>: MorexV3 only.</li>
                            
                        </ul>
                        
                        <br/>We shall be pleased to add
                        any dataset you suggest to the web application, granted that its use is free and public.
                        <br/><br/>
                """.format(base_url))
        
        ## ALIGN SEQUENCES
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link"  href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="align_sequences">Align sequences</h2>
                        
                        <br/>
                        
                        The "Align sequences" tool allows searching the map position of <strong>FASTA formatted sequences</strong> through alignment.
                        This process is slower than "Find markers", but allows adjusting the alignment parameters as needed and searching
                        for any DNA sequences.
                        
                        <br/><br/>
                        
                        Some of the features of "Align sequences" are:
                        
                        <ul class="help_list">
                            <li>
                            Barleymap results are map positions, which may come from different sequence references,
                            which are searched in a pan-genome or multi-reference fashion.
                            </li>
                            
                            <li>
                            It allows using different alignment algorithms, what makes possible to search for sequences with and without introns.
                            </li>
                            
                            <li>
                            Most of the details of this process are hidden from the user, who is interested only in the map and its map positions.
                            </li>
                        </ul>
                        
                        As such, most of the <strong>parameters</strong> are the equivalent to those explained for the "Find markers" tool above.
                        As in "Find markers", the user has to choose a <strong>map</strong> (or maps). Note that when the user chooses a map, he is actually choosing
                        all the <strong>sequence references</strong> associated to that map (in the internal Barleymap configuration),
                        as references for performing the alignments.
                        
                        <br/><br/>
                        
                        In "Align sequences" the user can choose different options for the <strong>alignment algorithm</strong>,
                        under the option "Choose an action".
                        
                        <ul class="help_list">
                            <li>
                            cdna: it is the recommended option, specially when all the queries come from sequences which could have introns.
                            For example, those from CDS or from markers produced from RNAseq data. All the alignments are performed
                            using the GMAP aligner<sup>[12][4]</sup>.
                            </li>
                            
                            <li>
                            genomic: it uses the most popular alignment tool, BLASTN<sup>[13][3]</sup>, to perform all the alignments.
                            </li>
                            
                            <li>
                            auto: every query is searched with GMAP. For those queries without hits, the search is repeated with BLASTN.
                            </li>
                        </ul>
                        
                        Note that the user can choose also the parameters which define minimum thresholds for results of alignment to be reported.
                        The <strong>minimum identity</strong> of alignment can be set with the "min. id." parameter,
                        whereas the <strong>minimum query coverage</strong> in the alignment
                        can be set with the "min. query cov." parameter.
                        Any alignment result with one of those parameters smaller than the thresholds will be discarded by barleymap and thus not reported in
                        the output tables.
                        
                        <br/><br/>
                        
                        Besides that, Barleymap is able to use 3 different algorithms when searching maps which have more than one
                        database associated to it. The details of how these algorithms work can be found
                        <a href="https://github.com/Cantalapiedra/barleymap#4111-alignment-algorithm">here</a>.
                        Here, just a brief description of the maps and databases included in this Barleymap web application,
                        and the algorithms used on them, is provided.
                        
                        <br/><br/>
                        
                        <h3 id="references_included">References included in Barleymap web</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                        <ul class="help_list">
                            <li><strong>Morex Genome</strong><sup>[3]</sup></li>
                                <br/>
                                
                                The Morex Genome is an actual genome assembly. Most of the datasets precomputed in Barleymap web
                                are available for this reference (one exception, the IBSC2012 BAC contigs). The main datasets
                                associated to this physical map are the IBSC2016 HC and LC genes (the "HORVUs"),
                                the Illumina 50K markers ("JHIs", "SCRIs", etc.), the Morex WGS contigs and the NCBI genes.
                                
                                <br/><br/>
                            <li><strong>POPSEQ map</strong><sup>[2]</sup></li>
                                <br/>
                                
                                The POPSEQ map is a genetic map with Morex WGS contigs anchored to it. The main datasets
                                associated to this map are the IBSC2012 HC and LC genes (the "MLOCs"),
                                the Illumina 50K markers ("JHIs", "SCRIs", etc.), and the Morex WGS contigs.
                                
                                <br/><br/>
                            <li><strong>IBSC2012 genetic/physical map</strong><sup>[1]</sup></li>
                                <br/>
                                
                                The IBSC2012 genetic and physical map has sequences of different nature anchored to it:
                                <br/>
                                <ul class="help_list">
                                    <li>Three <i>WGS</i> assemblies from different cultivars: Morex, Barke and Bowman.</li>
                                    <li>Morex cultivar sequenced BAC contigs.</li>
                                    <li>Morex cultivar BAC End sequences.</li>
                                </ul>
                                <br/>
                                
                                When a search is performed against the IBSC2012 map
                                an <strong>"exhaustive" algorithm</strong> (see Figure below) is used.
                                First, the queries are aligned against the first reference, using GMAP, BLASTN or both
                                depending on the aligner chosen (see above discussion about parameters of "Align sequences").
                                For every query with a hit in the reference a map position is retrieved.
                                Those queries without a map position are searched in the second reference.
                                This is repeated until all the queries have a map position or all the references have
                                been used once as reference.
                                The order in which databases are used as alignment target is the same as in the list above.
                        </ul>
                        <br/>
                        """.format(base_url))
        
        # PIPELINE IMAGE
        output_buffer.append("""
                        <br/>
                        <center><img width="499" height="526" style="border:none;" src="{0}"/></center>
                        <br/>
                        """.format(base_url+"/img/barleymap_popseq.pipeline_2.png"))
        
        
        ## LOCATE BY POSITION
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="locate_by_position">Locate by position</h2>
                        
                        <br/>
                        
                        The "Locate by position" tool allows examining the regions of <strong>specific map positions</strong>,
                        mainly with the purpose of checking which genes, markers or other loci are present in those regions.
                        
                        <br/><br/>
                        
                        The input data are "tuples", with chromosome (or contig) and position (local position within the chromosome or contig)
                        in basepairs or centimorgans (e.g. chr1H 100200).
                        
                        <br/><br/>
                        
                        All the other <strong>parameters</strong> are identical to those in "Find markers".
                        
                        <br/><br/>
                        
                """.format(base_url))
        
        ## OUTPUT
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="barleymap_output">Barleymap output</h2>
                        
                        <br/>
                        
                        On top of the results page, Barleymap outputs a list of maps selected by the user.
                        He can use the links on that list to navigate to the results of a specific map.
                        
                        <br/><br/>
                        
                        For every map which the user selected, Barleymap shows up to five tables of results:
                        
                        <ul class="help_list">
                            <li>
                            <a href="#results_map">Map</a>
                            </li>
                            
                            <li>
                            <a href="#results_markers">Map with markers</a>
                            </li>
                            
                            <li>
                            <a href="#results_genes">Map with genes</a>
                            </li>
                            
                            <li>
                            <a href="#results_anchored">Map with anchored elements</a>
                            </li>
                            
                            <li>
                            <a href="#results_unmapped_unaligned">Unmapped markers</a>
                            </li>
                            
                            <li>
                            <a href="#results_unmapped_unaligned">Unaligned markers</a>
                            </li>
                        </ul>
                        
                        <h3 id="results_map">Map</h3>
                        <a class="top_link"  href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                            <br/>
                            
                            The first result shown by Barleymap is a <strong>graphical representation</strong> of the seven barley chromosomes.
                            Queries with map position are shown on top of those chromosomes.
                            Using the magnifying glass button, the user can toggle between complete chromosomes or just the mapped region.
                            
                            <br/><br/>
                            
                            Below the graphical representation is the <strong>"Map"</strong> table, with the next fields:
                            
                            <ul class="help_list">
                                <li>Marker: identifier of the query sequence, either the user supplied value in "Find markers", the FASTA header
                                of the sequence in "Align sequences", or an arbitrary code "chromosome_position" created in "Locate by position".
                                </li>
                                <li>chr: chromosome (or contig or equivalent).</li>
                                <li>cM: centimorgans position. Only for anchored maps with cM positions (IBSC2012 and POPSEQ).</li>
                                <li>bp: basepairs position. Only for anchored maps with bp positions (IBSC2012).</li>
                                <li>start: basepairs starting position. Only for physical maps (MorexGenome).</li>
                                <li>end: basepairs ending position. Only for physical maps (MorexGenome).</li>
                                <li>strand: whether the query aligns to the target strand (+) or to the complementary strand (-). Only for physical maps (MorexGenome).</li>
                                <li>multiple positions: whether the current query sequence has more than one different mapping position in the current map.
                                    <br/>This field is shown only if the "Markers with multiple mappings" option has been selected.
                                    <br/>
                                </li>
                                <li>other alignments: whether the current query sequence has other alignment targets which lack map position.
                                    <br/>At least one unmapped alignment should be found for such query.
                                </li>
                            </ul>
                        
                        <h3 id="results_markers">Map with markers</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                            <br/>
                            
                            The <strong>Map with markers</strong> table shows the mapping results along with the genetic markers that are
                            located in the same positions (or regions if the search is extended). The table has the same fields as the Map table.
                        
                        <h3 id="results_genes">Map with genes</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                            <br/>
                            
                            The <strong>Map with genes</strong> table shows the mapping results along with the genes that are
                            located in the same positions (or regions if the search is extended). The table has all the fields of the previous tables,
                            plus some additional fields, related to functional annotation of genes:
                            
                            <ul class="help_list">
                                <li>Gene class: High Confidence or Low Confidence classification.</li>
                                <li>Description: human-readable description of the gene.</li>
                                <li>InterPro: IPR identifiers for the gene.</li>
                                <li>GeneOntologies: GO identifiers for the gene.</li>
                                <li>PFAM: Protein Families identifiers for the gene.</li>
                            </ul>
                        
                        <h3 id="results_anchored">Map with anchored elements</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                            <br/>
                            
                            The <strong>Map with anchored elements</strong> table shows the mapping results along with the elements that are
                            located in the same positions (or regions if the search is extended). In this case, they are not genes or markers;
                            anchored elements have map position but often lack biological meaning (e.g. WGS contigs, BAC contigs, etc.).
                            The table has the same fields as the Map and the Map with markers tables.
                        
                        
                        
                        <h3 id="results_unmapped_unaligned">Unmapped and unaligned markers</h3>
                        <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                        
                            <br/>
                            
                            In addition to the mapping results, two more tables are shown for each map.
                            
                            <ul class="help_list">
                                <li><strong>Unmapped</strong>: shows those queries which have an alignment hit (field "Target ID").</li>
                                    Note that queries in this table could still have map position, through a different alignment.
                                <li><strong>Unaligned</strong>: shows those queries which lack alignment hit (and thus map position).</li>
                            </ul>
                            
                        <br/>
            """.format(base_url))
        
        ## CONFIDENTIALITY
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="confidentiality">Confidentiality</h2>
                    
                        <br/>
			While Barleymap uses HTTPS by default, we can not guarantee the security of the data used with the web tool.
                        <br/><br/>
                        Should this naïve confidentiality be not acceptable to some users, we would recommend installing the
                        <a href="https://github.com/Cantalapiedra/barleymap">standalone barleymap</a> version,
                        or setting up their own instace of
                        <a href="https://github.com/Cantalapiedra/barleymap_web">barleymap web</a> version. 
                        <br/><br/>
            """.format(base_url))
        
        ## DISCLAIMER
        
        output_buffer.append("""
                    <hr/>
                    <br/>
                    <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="disclaimer">Disclaimer</h2>
                        <br/>
                        This service is available AS IS and at your own risk.
                        EEAD/CSIC do not give any representation or warranty nor assume
                        any liability or responsibility for the service or the results posted
                        (whether as to their accuracy, completeness, quality or otherwise).
                        Access to the service is available free of charge for ordinary use
                        in the course of academic research.
                        <br/><br/>
                    <hr/>
                <!--</section>-->
                <br/>
            """.format(base_url))
        
        ## APPENDIX
        
        output_buffer.append("""
                <br/>
                <a class="top_link" href="#"><img style="width:10px;height:10px;border:none;" src="{0}/img/top.jpg"/></a>
                    <h2 id="references">References</h2>
                <br/>
                <!--<section class="help_section">-->
                
                    <cite><sup>[1]</sup><a href="http://doi.org/10.1038/nature11543"
                                            target="_blank">IBSC 2012</a></cite>
                    <br/>
                    <cite><sup>[2]</sup><a href="http://doi.org/10.1111/tpj.12319"
                                            target="_blank">Mascher et al. 2013</a></cite>
                    <br/>
                    <cite><sup>[3]</sup><a href="http://doi.org/10.1038/nature22043"
                                           target="_blank">Mascher et al. 2017</a></cite>
                    <br/>
                    <cite><sup>[4]</sup><a href="https://doi.org/10.1186/1471-2164-10-582"
                                           target="_blank">Close et al. 2009</a></cite>
                    <br/>
                    <cite><sup>[5]</sup><a href="http://doi.org/10.1038/ng.2447"
                                           target="_blank">Comadran et al. 2012</a></cite>
                    <br/>
                    <cite><sup>[6]</sup><a href="https://doi.org/10.3389/fpls.2017.01792"
                                           target="_blank">Bayer et al. 2017</a></cite>
                    <br/>
                    <cite><sup>[7]</sup><a href="https://doi.org/10.1073/pnas.0401076101"
                                           target="_blank">Wenzl et al. 2004</a></cite>
                    <br/>
                    <cite><sup>[7']</sup><a href="http://www.diversityarrays.com/dart-map-sequences"
                                           target="_blank">www.diversityarrays.com</a></cite>
                    <br/>
                    <cite><sup>[8]</sup><a href="https://doi.org/10.1007/978-1-61779-870-2_5"
                                           target="_blank">Kilian et al. 2012</a></cite>
                    <br/>
                    <cite><sup>[9]</sup><a href="https://doi.org/10.1371/journal.pone.0032253"
                                           target="_blank">Poland et al. 2012</a></cite>
                    <br/>
                    <cite><sup>[10]</sup><a href="https://doi.org/10.1104/pp.110.171579"
                                           target="_blank">Matsumoto et al. 2011</a></cite>
                    <br/>
                    <cite><sup>[11]</sup><a href="http://harvest.ucr.edu"
                                           target="_blank">HarvEST</a></cite>
                    <br/>
                    <cite><sup>[12]</sup><a href="https://doi.org/10.1093/bioinformatics/bti310"
                                            target="_blank">Wu and Watanabe 2005</a></cite>
                    <br/>
                    <cite><sup>[13]</sup><a href="https://doi.org/10.1016/S0022-2836(05)80360-2"
                                            target="_blank">Altschul et al. 1990</a></cite>
                    <br/>
                    <cite><sup>[14]</sup><a href="https://doi.org/10.1093/plcell/koab077"
                                            target="_blank">Mascher et al. 2021</a></cite>
                    <br/>
                    <cite><sup>[15]</sup><a href="https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-6243-7"
                                            target="_blank">Rapazote-Flores et al. 2019</a></cite>
                    <br/>
                    <cite><sup>[16]</sup><a href="https://www.nature.com/articles/s41597-021-00872-4"
                                            target="_blank">Milne et al. 2021</a></cite>
                    <br/>
                </section>
                <br/>
                <hr/>
            </article>
            """.format(base_url))
        
        output_buffer.append("""
            <a href="{0}"><img style="width:5%;height:5%;border:none;" src="{1}" alt="back"/></a>
        </section> <!-- content -->
        """.format(base_url+"/", base_url+"/img/back.gif"))
        
        return "".join(output_buffer)

## END
