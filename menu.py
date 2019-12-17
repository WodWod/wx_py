#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 实验功能
#   1.文艺青年相亲指南
# 游记
# 我的小站

menuDict = [
            {
            'id':'1',
            'name':'实验功能',
            # 'response':{'type':'text','content':'还没写...'},
            'child':[
                        {
                            'id':'1a',
                            'name':'文艺青年相亲指南',
                            'response':{'type':'image','content':'RaBXyHYVj5Fq-Ijt5XhS-XPndEjPgIvm-e_FPfK5XrE'}
                        }
                ]
            },
            {
            'id':'2',
            'name':'游记',
            'response':{'type':'text','content':'还没写...'},
            'child':[
                        {
                            'id':'21',
                            'name':'骑行',
                            'child':[
                                     {
                                         'id':'21a',
                                         'name':'骑行·海南',
                                         'response':{'type':'text','content':'还没开始...'}
                                     }
                                ]
                        },
                        {
                            'id':'22',
                            'name':'公园',
                            'child':[
                                     {
                                         'id':'22a',
                                         'name':'公园·尖山湖',
                                         'response':{'type':'text','content':'还没写...'}
                                     }
                                ]
                        }
                ]
            },
            {
            'id':'3',
            'name':'我的小站',
            'response':{'type':'text','content':'www.onepieceofsu.cn'}
            },
           ]
def response(content):
    content = str(content).lower().strip()
    return searchLevel(content)
    # print('response:',searchLevel(content))
    
def searchLevel(content):
    if content == '0':
        response = ''
        for item_1 in menuDict:
            response += item_1['id']+'.'+item_1['name']
        return response
    elif len(content)==1 and  not content == '0':
        response = ''
        for item_1 in menuDict:
            if item_1['id'] == content:
                if not item_1.get('response'):
                    for item_2 in item_1['child']:
                        response += item_2['id'] +'.'+item_2['name']
                else:
                    response = item_1['response']['type']+ '|' + item_1['response']['content']
        return response

    elif len(content)==2:
        first = content[0:1]
        second = content
        response = ''
        for item_1 in menuDict:
            if item_1['id'] == first:
                if not item_1.get('response'):
                    for item_2 in item_1['child']:
                        if item_2['id'] == second:
                            if not item_2.get('response'):
                                for item_3 in item_2['child']:
                                    response = item_3['id'] + '.' + item_3['name']
                            else:
                                response = item_2['response']['type']+ '|' + item_2['response']['content']               
        return response

    elif len(content)==3:
        first = content[0:1]
        second = content[0:2]
        third = content
        response = ''
        for item_1 in menuDict:
            if item_1['id'] == first:
                if not item_1.get('response'):
                    for item_2 in item_1['child']:
                        if item_2['id'] == second:
                            if not item_2.get('response'):
                                for item_3 in item_2['child']:
                                    if not item_3.get('response'):
                                        pass
                                    else:
                                        if item_3['id'] == third:
                                            response = item_3['response']['type']+ '|' + item_3['response']['content']
        return response
                

response('0')
response('1')
response('2')
response('3')



# from urllib import request,parse
# import getAccessToken

# class Menu(object):
#     def __init__(self):
#         pass
#     def create(self,postData,accessToken):
#         postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
#         postData = parse.urlencode(postData)
#         with request.urlopen(postUrl,data=postData.encode('utf-8')) as f:
#             print(f.read())

# if __name__ == '__main__':
    # myMenu = Menu()
    # postJson = {
    #     'button':[
    #         {
    #             'name':'实验功能',
    #             'sub_button':[
    #                 {
    #                 'type':'click',
    #                 'name':'文艺青年相亲指南',
    #                 'key':'doubanMeeting'
    #                 }
    #             ]
    #         },
    #         {
    #             'name':'游记',
    #             'sub_button':[
    #                 {
    #                 'type':'click',
    #                 'name':'游·公园',
    #                 'key':'parkTour'
    #                 },
    #                 {
    #                 'type':'click',
    #                 'name':'游·骑行',
    #                 'key':'bicycleTour'
    #                 }
    #             ]
    #         },
    #         {
    #             'name':'我的小站',
    #             'type':'view',
    #             'url':'http://onepieceofsu.cn'
    #         },
    #     ]
    # }
     
    # accessToken=getAccessToken.getData()
    # myMenu.create(postJson,accessToken)
