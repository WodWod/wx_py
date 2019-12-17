#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request,parse
import getAccessToken
import json

class MediaList(object):
    def  GET(self):
        accessToken=getAccessToken.getData()
        postUrl='https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=%s'  % accessToken
        TYPE='news'
        OFFSET='0'
        COUNT='20'
        data={
            "type":TYPE,
            "offset":OFFSET,
            "count":COUNT
        }
        postData = json.dumps(data)
        with request.urlopen(postUrl,data=postData.encode('utf-8')) as f:
            response =  json.loads(f.read().decode('utf-8'))
            list1 = '图文消息列表: \n'
            print(response)
            for media in response['item']:
               list1 += ('media_id:%s\ntitle:%s\ndigest:%s\nthumb_url:%s\nurl:%s\n' % (media['media_id'],media['content']['news_item'][0]['title'],media['content']['news_item'][0]['digest'],media['content']['news_item'][0]['thumb_url'],media['content']['news_item'][0]['url'])) 

            return list1.encode('gb2312')