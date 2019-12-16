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
                    replyMsg= reply.TextMsg(toUser,fromUser,content)
                    return replyMsg.send()
                elif recMsg.MsgType=='image':
                    mediaId = recMsg.MediaId
                    replyMsg= reply.ImageMsg(toUser,fromUser,mediaId)
                    return replyMsg.send()
            else:
                print('不处理')
                return 'success'

        except BaseException as e:
            print('Error:',e)
            return 'Error'