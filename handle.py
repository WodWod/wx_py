#!/usr/bin/python
# -*- coding: UTF-8 -*-

import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            data=web.input()
            if len(data)==0:
                return 'this is a wx handle'
            signature=data.signature
            timestamp=data.timestamp
            nonce=data.nonce
            echostr=data.echostr
            token='hellosu'

            list= [token,timestamp,nonce]
            list.sort()
            sha1=hashlib.sha1()
            map(sha1.update,list)
            hascode = sha1.hexdigest()
            print('handle/GET func: hashcode, signature: ',hascode,signature)
            if hascode==signature:
                return echostr
            else:
                return ''
        except BaseException as e:
            print('Error:',e)
            return 'Error'
            