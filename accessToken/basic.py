#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import time
import json

class Basic:
    def __init__(self):
        self.__accessToken=''
        self.__leftTime=0

    def __real_get_access_token(self):
        appId='wx1b6ea759f3717c05'
        appSecret='8ca156f62ae8c7626493b13d03737222'
        postUrl=('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'% (appId,appSecret))
        with request.urlopen(postUrl) as f:
            urlResp = json.loads(f.read())
            self.__accessToken=urlResp['accessToken']
            self.__leftTime=urlResp['expires_in']
    
    def get_access_token(self):
        if(self.__leftTime<10):
            self.__real_get_access_token()
        
        return self.__accessToken

    def run(self): 
        while True:
            if self.__leftTime>10:
                time.sleep(2)
                self.__leftTime-=2
            else:
                self.__real_get_access_token()
            
 
