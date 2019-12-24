#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import web
from recommend import Recommend

class Submit(object):
    def POST(self):
        post_data=web.data()
        handle = Recommend(post_data)
        return handle.get_data()
