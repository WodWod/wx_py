#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import web 

from basic import Basic

urls = (
    '/get_access_token', 'Handle',
)

class Handle(object):
    def GET(self):
        try:
            data=basic.get_access_token()
            return data
        except BaseException as e:
            print('Error:',e)
            return 'Error'

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()  
    basic=Basic()
    basic.run()