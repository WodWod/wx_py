#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import web
import mysql.connector 
import json
from config import config 

conn = mysql.connector.connect(host=config['host'],user=config['user'], password=config['password'], database=config['database'])
cursor = conn.cursor()

class InputSuggest(object):
    def GET(self):
        try:
            data=web.input()
            global conn,cursor
            cursor.execute('select subject_num,name from subject where type=%s and name like %s limit 10',[data.type,'%'+data.name+'%'])
            values = cursor.fetchall()
            if len(values)>0:
                return json.dumps(values)
            else:
                return '[]'
        except BaseException as e:
            print("Error:",e) 
            conn = mysql.connector.connect(host=config['host'],user=config['user'], password=config['password'], database=config['database'])
            cursor = conn.cursor()
            
