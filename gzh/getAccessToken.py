#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

def getData():
    getUrl='http://122.51.163.46:1021/get_access_token'
    with request.urlopen(getUrl) as f:
        return f.read().decode('utf-8')