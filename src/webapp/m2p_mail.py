#!/usr/bin/env python
# -*- coding: utf-8 -*-

# m2p_mail.py is part of Barleymap web app.
# Copyright (C)  2013-2014  Carlos P Cantalapiedra.
# (terms of use can be found within the distributed LICENSE file).

import sys, smtplib, traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from barleymapcore.m2p_exception import m2pException

MAIL_HOST = "MAIL_HOST"
MAIL_PORT = "MAIL_PORT"
MAIL_SENDER = "MAIL_SENDER"
MAIL_USER = "MAIL_USER"
MAIL_PASS = "MAIL_PASS"

def send_files(form, filenames, filedescs, email_conf):
    try:
        email_to = form.get_email_to()
        
        sys.stderr.write("M2P: Sending email to "+email_to+"\n")
        
        params = form.as_params_string() # This should be a string with one line per parameter "name: value"
        
        email_dict = __load_email_dict(email_conf)
        # Create the enclosing (outer) message
        email_from = email_dict[MAIL_SENDER]
        
        outer = __create_outer_msg(email_from, email_to, 'Markers mapped to barleymap')
        
        # Main Text
        email_text = MIMEText(params, _subtype='plain')
        outer.attach(email_text)
        
        # Attachments
        i = 0
        for file_name in filenames:
            file_desc = filedescs[i]
            sys.stderr.write("m2p_mail: "+file_name+"-->"+file_desc+"\n")
            __add_file(file_name, outer, file_desc+".csv")
            
            i+=1
        
        # Connection to server and delivery
        __send(email_from, email_to, outer, email_dict)
    
    except m2pException:
        raise
    except Exception:
        traceback.print_exc(file=sys.stderr)
        raise m2pException("Error sending email")
    
    return

def __load_email_dict(email_conf):
    email_dict = {}
    
    for email_line in open(email_conf, 'r'):
        email_data = email_line.strip().split(" = ")
        email_dict[email_data[0]] = email_data[1]
        #sys.stderr.write("m2p_mail: "+email_data[0]+"\t"+email_data[1]+"\n")
    
    return email_dict
    

def __create_outer_msg(email_from, email_to, subject):
    
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = subject
    outer['To'] = email_to
    outer['From'] = email_from
    
    return outer

def __add_file(file_name, outer, map_name):
    # Attached CSV
    fp = open(file_name)
    try:
        msg = MIMEText(fp.read(), _subtype="csv")
    except Exception:
        traceback.print_exc(file=sys.stderr)
        raise m2pException("Error opening file to send by email.")
    finally:
        fp.close()
    
    msg.add_header('Content-Disposition', 'attachment', filename=map_name)
    outer.attach(msg)
    
    return

def __send(email_from, email_to, outer, email_dict):
    # Connection to server and delivery
    s = smtplib.SMTP()
    try:
        s.connect(email_dict[MAIL_HOST], int(email_dict[MAIL_PORT]))
        s.starttls()
        s.login(email_dict[MAIL_USER], email_dict[MAIL_PASS])
        s.sendmail(email_from, [email_to], outer.as_string())
    except Exception:
        traceback.print_exc(file=sys.stderr)
        raise m2pException("Error sending email to "+email_to+".")
    finally:
        s.close()
    
    return

## END