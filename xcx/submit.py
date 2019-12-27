#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import web
import json
from xcx.recommend import Recommend

class Submit(object):
    def POST(self):
        post_data=web.data().decode('utf-8')
        handle = Recommend(post_data)
        return json.dumps(handle.get_data())
