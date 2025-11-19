#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FormsFactory.py is part of Barleymap web app.
# Copyright (C) 2017  Carlos P Cantalapiedra.
# Copyright (C) 2025 Bruno Contreras Moreira and Joan Sarria
# (terms of use can be found within the distributed LICENSE file).

#import sys

class FormsFactory(object):
    
    @staticmethod
    def get_align_form_new(query = "", multiple = "", sort = "",
                           show_markers = "", show_genes = "", show_anchored = "",
                           show_main = "", show_how = "",
                           extend = "", extend_cm = "", extend_bp = "",
                           maps = "", graphs="", send_email = "", email_to = "", user_file = None,
                           aligner = "", threshold_id = "", threshold_cov = ""):
        
        form = AlignForm()
        
        form.set_parameters(query, multiple, sort,
                           show_markers, show_genes, show_anchored,
                           show_main, show_how,
                           extend, extend_cm, extend_bp,
                           maps, graphs, send_email, email_to, user_file)
        
        form.set_aligner(aligner)
        form.set_threshold_id(threshold_id)
        form.set_threshold_cov(threshold_cov)
        
        return form
    
    @staticmethod
    def get_align_form_empty(DEFAULT_GENES_WINDOW_CM, DEFAULT_GENES_WINDOW_BP,
                             DEFAULT_MAPS, DEFAULT_ALIGNER,
                             DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV):
        
        align_form = AlignForm()
        
        align_form.set_extend_cm(DEFAULT_GENES_WINDOW_CM)
        align_form.set_extend_bp(DEFAULT_GENES_WINDOW_BP)
        align_form.set_maps(DEFAULT_MAPS)
        align_form.set_aligner(DEFAULT_ALIGNER)
        align_form.set_threshold_id(DEFAULT_THRESHOLD_ID)
        align_form.set_threshold_cov(DEFAULT_THRESHOLD_COV)
        
        return align_form
    
    @staticmethod
    def get_align_form_session(session, DEFAULT_ALIGNER, DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV):
        align_form = None
        
        align_form = AlignForm.init_from_session(session, DEFAULT_ALIGNER, DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV)
        
        return align_form
   
    @staticmethod
    def get_graph_form_new(query = "", multiple = "", sort = "",
                           show_markers = "", show_genes = "", show_anchored = "",
                           show_main = "", show_how = "",
                           extend = "", extend_cm = "", extend_bp = "",
                           maps = "", grahps="", send_email = "", email_to = "", user_file = None,
                           aligner = "", threshold_id = "", threshold_cov = ""):

        form = GraphForm()

        form.set_parameters(query, multiple, sort,
                           show_markers, show_genes, show_anchored,
                           show_main, show_how,
                           extend, extend_cm, extend_bp,
                           maps, graphs, send_email, email_to, user_file)

        form.set_aligner(aligner)
        form.set_threshold_id(threshold_id)
        form.set_threshold_cov(threshold_cov)

        return form

    @staticmethod
    def get_graph_form_empty(DEFAULT_GENES_WINDOW_CM, DEFAULT_GENES_WINDOW_BP,
                             DEFAULT_GRAPHS, DEFAULT_ALIGNER_GRAPH,
                             DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV):

        align_form = GraphForm()

        align_form.set_extend_cm(DEFAULT_GENES_WINDOW_CM)
        align_form.set_extend_bp(DEFAULT_GENES_WINDOW_BP)
        align_form.set_graphs(DEFAULT_GRAPHS)
        align_form.set_aligner(DEFAULT_ALIGNER_GRAPH)
        align_form.set_threshold_id(DEFAULT_THRESHOLD_ID)
        align_form.set_threshold_cov(DEFAULT_THRESHOLD_COV)

        return align_form

    @staticmethod
    def get_graph_form_session(session, DEFAULT_ALIGNER_GRAPH, DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV):
        align_form = None

        align_form = GraphForm.init_from_session(session, DEFAULT_ALIGNER_GRAPH, DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV)

        return align_form

    @staticmethod
    def get_find_form_new(query = "", multiple = "", sort = "",
                           show_markers = "", show_genes = "", show_anchored = "",
                           show_main = "", show_how = "",
                           extend = "", extend_cm = "", extend_bp = "",
                           maps = "", graphs="", send_email = "", email_to = "", user_file = None):
        
        form = FindForm()
        
        form.set_parameters(query, multiple, sort,
                           show_markers, show_genes, show_anchored,
                           show_main, show_how,
                           extend, extend_cm, extend_bp,
                           maps, graphs, send_email, email_to, user_file)
        
        return form
    
    @staticmethod
    def get_find_form_empty(DEFAULT_GENES_WINDOW_CM, DEFAULT_GENES_WINDOW_BP, DEFAULT_MAPS):
        
        find_form = FindForm()
        
        find_form.set_extend_cm(DEFAULT_GENES_WINDOW_CM)
        find_form.set_extend_bp(DEFAULT_GENES_WINDOW_BP)
        find_form.set_maps(DEFAULT_MAPS)
        
        return find_form
    
    @staticmethod
    def get_find_form_session(session):
        find_form = None
        
        find_form = FindForm.init_from_session(session)
        
        return find_form
    
    @staticmethod
    def get_locate_form_new(query = "", multiple = "", sort = "",
                           show_markers = "", show_genes = "", show_anchored = "",
                           show_main = "", show_how = "",
                           extend = "", extend_cm = "", extend_bp = "",
                           maps = "", graphs = "", send_email = "", email_to = "", user_file = None):
        
        form = LocateForm()
        
        form.set_parameters(query, multiple, sort,
                           show_markers, show_genes, show_anchored,
                           show_main, show_how,
                           extend, extend_cm, extend_bp,
                           maps, graphs, send_email, email_to, user_file)
        
        return form
    
    @staticmethod
    def get_locate_form_empty(DEFAULT_GENES_WINDOW_CM, DEFAULT_GENES_WINDOW_BP, DEFAULT_MAPS):
        
        form = LocateForm()
        
        form.set_extend_cm(DEFAULT_GENES_WINDOW_CM)
        form.set_extend_bp(DEFAULT_GENES_WINDOW_BP)
        form.set_maps(DEFAULT_MAPS)
        
        return form
    
    @staticmethod
    def get_locate_form_session(session):
        form = None
        
        form = LocateForm.init_from_session(session)
        
        return form

class InputForm(object):
    
    ACTION = "action"
    SESSION = "session_token"
    QUERY = "query"
    MULTIPLE = "multiple"
    SORT = "sort"
    SHOW_MARKERS = "show_markers"
    SHOW_GENES = "show_genes"
    SHOW_ANCHORED = "show_anchored"
    SHOW_MAIN = "show_main"
    SHOW_HOW = "show_how"
    EXTEND = "extend"
    EXTEND_CM = "extend_cm"
    EXTEND_BP = "extend_bp"
    MAPS = "maps"
    GRAPHS = "graphs"
    SEND_EMAIL = "send_email"
    EMAIL_TO = "email_to"
    COLLAPSED_VIEW = "collapsed_view"
    USER_FILE = "user_file"
    
    _action = ""
    _query = ""
    _multiple = ""
    _sort = ""
    _show_markers = ""
    _show_genes = ""
    _show_anchored = ""
    _show_main = "" # show all features or just main (depending on which map, the main ones e.g.: Illumina50K)
    _show_how = "" # on intervals, on markers
    _extend = ""
    _extend_cm = ""
    _extend_bp = ""
    _maps = ""
    _graphs = ""
    _send_email = ""
    _email_to = ""
    _collapsed_view = True
    _user_file = None
    
    _is_empty = True
    
    def get_action(self, ):
        return self._action
    
    def set_action(self, action):
        self._action = action
    
    def get_query(self):
        return self._query
    
    def set_query(self, query):
        self._query = query
    
    def get_multiple(self):
        return self._multiple
    
    def set_multiple(self, multiple):
        self._multiple = multiple
    
    def get_sort(self):
        return self._sort
    
    def set_sort(self, sort):
        self._sort = sort
    
    def get_show_markers(self):
        return self._show_markers
    
    def set_show_markers(self, show_markers):
        self._show_markers = show_markers
    
    def get_show_genes(self):
        return self._show_genes
    
    def set_show_genes(self, show_genes):
        self._show_genes = show_genes
    
    def get_show_anchored(self):
        return self._show_anchored
    
    def set_show_anchored(self, show_anchored):
        self._show_anchored = show_anchored
    
    def get_show_main(self, ):
        return self._show_main
    
    def set_show_main(self, show_main):
        self._show_main = show_main
    
    def get_show_how(self, ):
        return self._show_how
    
    def set_show_how(self, show_how):
        self._show_how = show_how
    
    def get_extend(self):
        return self._extend
    
    def set_extend(self, extend):
        self._extend = extend
    
    def get_extend_cm(self):
        return self._extend_cm
    
    def set_extend_cm(self, extend_cm):
        self._extend_cm = extend_cm
    
    def get_extend_bp(self, ):
        return self._extend_bp
    
    def set_extend_bp(self, extend_bp):
        self._extend_bp = extend_bp
    
    def get_maps(self, ):
        return self._maps
    
    def set_maps(self, maps):
        self._maps = maps

    def get_graphs(self, ):
        return self._graphs

    def set_graphs(self, graphs):
        self._graphs = graphs
 
    def get_send_email(self, ):
        return self._send_email
    
    def set_send_email(self, send_email):
        self._send_email = send_email
    
    def get_email_to(self, ):
        return self._email_to
    
    def set_email_to(self, email_to):
        self._email_to = email_to
    
    def get_collapsed_view(self, ):
        return self._collapsed_view
    
    def set_collapsed_view(self, collapsed_view):
        self._collapsed_view = collapsed_view
    
    def get_user_file(self):
        return self._user_file
    
    def set_user_file(self, user_file):
        self._user_file = user_file
    
    def is_empty(self, ):
        return self._is_empty
    
    def set_empty(self, is_empty):
        self._is_empty = is_empty
    
    def set_session_input_form(self, session):
        
        session[self.SESSION] = self.SESSION
        session[self.ACTION] = self._action
        
        session[self.QUERY] = self.get_query()
        session[self.MULTIPLE] = self.get_multiple()
        session[self.SORT] = self.get_sort()
        session[self.SHOW_MARKERS] = self.get_show_markers()
        session[self.SHOW_GENES] = self.get_show_genes()
        session[self.SHOW_ANCHORED] = self.get_show_anchored()
        session[self.SHOW_MAIN] = self.get_show_main()
        session[self.SHOW_HOW] = self.get_show_how()
        
        if self.get_extend() == "1":
            session[self.EXTEND] = self.get_extend()
        else:
            session[self.EXTEND] = "0"
        
        session[self.EXTEND_CM] = self.get_extend_cm()
        session[self.EXTEND_BP] = self.get_extend_bp()
        session[self.MAPS] = self.get_maps()
        session[self.GRAPHS] = self.get_graphs()
        
        if self.get_send_email() == "1":
            session[self.SEND_EMAIL] = self.get_send_email()
        else:
            session[self.SEND_EMAIL] = "0"
            
        session[self.EMAIL_TO] = self.get_email_to()
        
        session[self.COLLAPSED_VIEW] = self.get_collapsed_view()
        
        return
    
    @staticmethod
    def init_from_session(session, form):
        
        if session[form.ACTION] == form.get_action():
            form._query = session.get(form.QUERY)
        else: # Comes from find action
            form._query = ""
        
        form._multiple = session.get(form.MULTIPLE)
        form._sort = session.get(form.SORT)
        form._show_markers = session.get(form.SHOW_MARKERS)
        form._show_genes = session.get(form.SHOW_GENES)
        form._show_anchored = session.get(form.SHOW_ANCHORED)
        form._show_main = session.get(form.SHOW_MAIN)
        form._show_how = session.get(form.SHOW_HOW)
        form._extend = session.get(form.EXTEND)
        form._extend_cm = session.get(form.EXTEND_CM)
        form._extend_bp = session.get(form.EXTEND_BP)
        form._maps = session.get(form.MAPS)
        form._graphs = session.get(form.GRAPHS)
        form._send_email = session.get(form.SEND_EMAIL)
        form._email_to = session.get(form.EMAIL_TO)
        form._user_file = session.get(form.USER_FILE)
        form._collapsed_view = session.get(form.COLLAPSED_VIEW)
        
        form._is_empty = False
        
        if session[form.ACTION] == "index":
            form.set_action("index")
        
        return form
    
    def set_parameters(self, query = "", multiple = "", sort = "",
                           show_markers = "", show_genes = "", show_anchored = "",
                           show_main = "", show_how = "",
                           extend = "", extend_cm = "", extend_bp = "",
                           maps = "", graphs = "", send_email = "", email_to = "", user_file = None):
        form = self
        
        form.set_query(query)
        form.set_multiple(multiple)
        form.set_sort(sort)
        show_markers = show_markers if show_markers else "0"
        form.set_show_markers(show_markers)
        show_genes = show_genes if show_genes else "0"
        form.set_show_genes(show_genes)
        show_anchored = show_anchored if show_anchored else "0"
        form.set_show_anchored(show_anchored)
        show_main = show_main if show_main else "0"
        form.set_show_main(show_main)
        form.set_show_how(show_how)
        form.set_extend(extend)
        form.set_extend_cm(extend_cm)
        form.set_extend_bp(extend_bp)
        form.set_maps(maps)
        form.set_graphs(graphs)
        form.set_send_email(send_email)
        form.set_email_to(email_to)
        form.set_collapsed_view(True)
        form.set_user_file(user_file)
        
        return
    
    def as_params_string_input_form(self, ):
        ret_value = []
        
        ret_value.append("Show queries with multiple hits: "+self.get_multiple())
        ret_value.append("Sort by: "+self.get_sort())
        ret_value.append("Show genes: "+self.get_show_genes())
        ret_value.append("Show markers: "+self.get_show_markers())
        ret_value.append("Show anchored features: "+self.get_show_anchored())
        ret_value.append("Show main: "+self.get_show_main())
        ret_value.append("Show how: "+self.get_show_how())
        ret_value.append("Extend search: "+self.get_extend())
        ret_value.append("Extend interval (cM): "+self.get_extend_cm())
        ret_value.append("Extend interval (bp): "+self.get_extend_bp())
        ret_value.append("Maps: "+",".join(self.get_maps()))
        ret_value.append("Graphs: "+",".join(self.get_graphs()))
        
        return "\n".join(ret_value)
    
    
class AlignForm(InputForm):

    ALIGNER = "aligner"
    THRESHOLD_ID = "threshold_id"
    THRESHOLD_COV = "threshold_cov"
    
    _action = "align"
    _aligner = ""
    _threshold_id = ""
    _threshold_cov = ""
    
    def __init__(self):
        pass
    
    @staticmethod
    def init_from_session(session, DEFAULT_ALIGNER, DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV):
        
        new_form = AlignForm()
        
        InputForm.init_from_session(session, new_form)
        
        if session[new_form.ACTION] != new_form.get_action():
            new_form._aligner = DEFAULT_ALIGNER
            new_form._threshold_id = DEFAULT_THRESHOLD_ID
            new_form._threshold_cov = DEFAULT_THRESHOLD_COV
        else:
            new_form._aligner = session.get(new_form.ALIGNER)
            new_form._threshold_id = session.get(new_form.THRESHOLD_ID)
            new_form._threshold_cov = session.get(new_form.THRESHOLD_COV)
        
        new_form._is_empty = False
        
        return new_form
    
    def set_session(self, session):
        
        self.set_session_input_form(session)
        
        session[self.ALIGNER] = self.get_aligner()
        session[self.THRESHOLD_ID] = self.get_threshold_id()
        session[self.THRESHOLD_COV] = self.get_threshold_cov()
        
        return
    
    def get_aligner(self, ):
        return self._aligner
    
    def set_aligner(self, aligner):
        self._aligner = aligner
    
    def get_threshold_id(self, ):
        return self._threshold_id
    
    def set_threshold_id(self, threshold_id):
        self._threshold_id = threshold_id
    
    def get_threshold_cov(self, ):
        return self._threshold_cov
    
    def set_threshold_cov(self, threshold_cov):
        self._threshold_cov = threshold_cov
    
    def as_params_string(self, ):
        ret_value = []
        
        ret_value.append(self.as_params_string_input_form())
        
        ret_value.append("Aligner: "+self.get_aligner())
        ret_value.append("Threshold Id: "+self.get_threshold_id())
        ret_value.append("Threshold_cov: "+self.get_threshold_cov())
        
        return "\n".join(ret_value)

class GraphForm(InputForm):

    ALIGNER = "aligner"
    THRESHOLD_ID = "threshold_id"
    THRESHOLD_COV = "threshold_cov"

    _action = "graph"
    _aligner = ""
    _threshold_id = ""
    _threshold_cov = ""

    def __init__(self):
        pass

    @staticmethod
    def init_from_session(session, DEFAULT_ALIGNER_GRAPH, DEFAULT_THRESHOLD_ID, DEFAULT_THRESHOLD_COV):

        new_form = GraphForm()

        InputForm.init_from_session(session, new_form)

        if session[new_form.ACTION] != new_form.get_action():
            new_form._aligner = DEFAULT_ALIGNER_GRAPH
            new_form._threshold_id = DEFAULT_THRESHOLD_ID
            new_form._threshold_cov = DEFAULT_THRESHOLD_COV
        else:
            new_form._aligner = session.get(new_form.ALIGNER)
            new_form._threshold_id = session.get(new_form.THRESHOLD_ID)
            new_form._threshold_cov = session.get(new_form.THRESHOLD_COV)

        new_form._is_empty = False

        return new_form

    def set_session(self, session):

        self.set_session_input_form(session)

        session[self.ALIGNER] = self.get_aligner()
        session[self.THRESHOLD_ID] = self.get_threshold_id()
        session[self.THRESHOLD_COV] = self.get_threshold_cov()

        return

    def get_aligner(self, ):
        return self._aligner

    def set_aligner(self, aligner):
        self._aligner = aligner

    def get_threshold_id(self, ):
        return self._threshold_id

    def set_threshold_id(self, threshold_id):
        self._threshold_id = threshold_id

    def get_threshold_cov(self, ):
        return self._threshold_cov

    def set_threshold_cov(self, threshold_cov):
        self._threshold_cov = threshold_cov

    def as_params_string(self, ):
        ret_value = []

        ret_value.append(self.as_params_string_input_form())

        ret_value.append("Aligner: "+self.get_aligner())
        ret_value.append("Threshold Id: "+self.get_threshold_id())
        ret_value.append("Threshold_cov: "+self.get_threshold_cov())

        return "\n".join(ret_value)    


class FindForm(InputForm):
    
    _action = "find"
    
    def __init__(self):
        pass
    
    @staticmethod
    def init_from_session(session):
        
        new_form = FindForm()
        
        InputForm.init_from_session(session, new_form)
        
        return new_form
    
    def set_session(self, session):
        
        self.set_session_input_form(session)
        
        return
    
    def as_params_string(self, ):
        ret_value = []
        
        ret_value.append(self.as_params_string_input_form())
        
        return "\n".join(ret_value)

class LocateForm(InputForm):
    
    _action = "locate"
    
    def __init__(self):
        pass
    
    @staticmethod
    def init_from_session(session):
        
        new_form = LocateForm()
        
        InputForm.init_from_session(session, new_form)
        
        return new_form
    
    def set_session(self, session):
        
        self.set_session_input_form(session)
        
        return
    
    def as_params_string(self, ):
        ret_value = []
        
        ret_value.append(self.as_params_string_input_form())
        
        return "\n".join(ret_value)

## END
