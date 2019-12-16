#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import web 

from basic import Basic

urls = (
    '/get_access_token', 'Handle',
)

basic=Basic()


class Handle(object):
    def GET(self):
        try:
            if not basic.hasInit:
                basic.run()  #需要调用一次来启动
            else:
                data=basic.get_access_token()
                return data
            
        except BaseException as e:
            print('Error:',e)
            return 'Error'

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()  
   