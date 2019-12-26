#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import ptvsd
# ptvsd.enable_attach(address = ('localhost', 8888))
# ptvsd.wait_for_attach()

import web 
from img_bg_list import ImgBgList
from input_suggest import InputSuggest
from submit import Submit

urls = (
    '/dbmeeting/get_img_bg', 'ImgBgList',
    '/dbmeeting/input_suggest', 'InputSuggest',
    '/dbmeeting/submit', 'Submit'
)

if __name__ == '__main__':
    # print('accessToken',getAccessToken.getData())
    app = web.application(urls, globals())
    app.run()
    