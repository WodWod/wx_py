#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import web
import mysql.connector 
import json
from xcx.config import config 

conn = mysql.connector.connect(host=config['host'],user=config['user'], password=config['password'], database=config['database'])
cursor = conn.cursor()

class ImgBgList(object):
    def GET(self):
        # data=web.input()
        global conn,cursor
        try:
            cursor.execute('select distinct(img_src),person_name from movie_person order by person_name limit 200')
        except BaseException as e:
            print("ImgBgList Error:",e) 
            conn = mysql.connector.connect(host=config['host'],user=config['user'], password=config['password'], database=config['database'])
            cursor = conn.cursor()
            cursor.execute('select distinct(img_src),person_name from movie_person order by person_name limit 200')
        values = cursor.fetchall()
        list=[]
        for value in values:
            list.append(value[0])
        return json.dumps(list)
            
            
         