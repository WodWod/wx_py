#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import web
import reply
import receive
from menu import response

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
            hashcode = sha1.hexdigest()
            print('handle/GET func: hashcode, signature: ',hashcode,signature)
            if hashcode==signature:
                return echostr
            else:
                return ''
        except BaseException as e:
            print('Error:',e)
            return 'Error'
            
    def POST(self):
        try:
            webData=web.data()
            print("Handle Post webData is ",webData)
            
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg,receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType=='text': 
                    content = response(recMsg.Content)
                    if content == '':
                        content = '没有查询到序号对应内容\n回复0可查询菜单主页'
                    if  isinstance(content,dict) :
                        responseType = content['type']
                        if responseType == 'text':
                            replyMsg= reply.TextMsg(toUser,fromUser,content['content'])
                        elif responseType == 'image':
                            replyMsg= reply.ImageMsg(toUser,fromUser,content['id'])
                        elif responseType == 'news':
                            replyMsg= reply.NewsMsg(toUser,fromUser,**content)
                    else:
                        replyMsg= reply.TextMsg(toUser,fromUser,content)
                    return replyMsg.send()
                elif recMsg.MsgType=='image':
                    mediaId = recMsg.MediaId
                    replyMsg= reply.ImageMsg(toUser,fromUser,mediaId)
                    return replyMsg.send()
                elif recMsg.MsgType=='event':
                    if recMsg.EventType=='subscribe': #订阅事件
                        pre = '欢迎关注无名小屋\n'
                        content = response('0') + '\n'
                        end = '回复序号即可获取下级菜单或详情'
                        content = pre + content + end
                        replyMsg= reply.TextMsg(toUser,fromUser,content)
                        return replyMsg.send()
            else:
                print('不处理')
                return 'success'

        except BaseException as e:
            print('Error:',e)
            return 'Error'