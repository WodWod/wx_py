#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import ptvsd
# ptvsd.enable_attach(address = ('localhost', 8888))
# ptvsd.wait_for_attach()

import web 
import hashlib
import getAccessToken

from handle import Handle

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    # print('accessToken',getAccessToken.getData())
    app = web.application(urls, globals())
    app.run()
    