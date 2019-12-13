#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request,parse
import getAccessToken

class Menu(object):
    def __init__(self):
        pass
    def create(self,postData,accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        postData = parse.urlencode(postData)
        with request.urlopen(postUrl,data=postData.encode('utf-8')) as f:
            print(f.read())

if __name__ == '__main__':
    myMenu = Menu()
    postJson = {
        'button':[
            {
                'name':'实验功能',
                'sub_button':[
                    {
                    'type':'click',
                    'name':'文艺青年相亲指南',
                    'key':'doubanMeeting'
                    }
                ]
            },
            {
                'name':'游记',
                'sub_button':[
                    {
                    'type':'click',
                    'name':'游·公园',
                    'key':'parkTour'
                    },
                    {
                    'type':'click',
                    'name':'游·骑行',
                    'key':'bicycleTour'
                    }
                ]
            },
            {
                'name':'我的小站',
                'type':'view',
                'url':'http://onepieceofsu.cn'
            },
        ]
    }
     
    accessToken=getAccessToken.getData()
    myMenu.create(postJson,accessToken)
# 实验功能
#   1.文艺青年相亲指南
# 游记
# 我的小站