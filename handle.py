#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            data=web.input()
            if len(data)==0:
                return '这是一个微信认证逻辑'
            
        except:
            