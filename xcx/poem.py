#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

data = [
    {'data':'我喜欢站在未完工的两广路上喊你的名字','class':'content'},
    {'data':'除你之外我对眼前的整座城市一无所知','class':'content'},
    {'data':'我热爱你的心灵就像是那个下午的阳光','class':'content'},
    {'data':'我喜欢走你走过的楼梯由下到上','class':'content'},
    {'data':'那个夏天在我记忆里犹如一幅空白的画','class':'content'},
    {'data':'你送我的橡皮在我送你的白纸上轻轻涂擦','class':'content'},
    {'data':'我背向你用手中湿润的杯子去接取太阳','class':'content'},
    {'data':'然后紧闭双眼默默地想你穿裙子的模样','class':'content'},
    {'data':'---《给郁结的诗》','class':'remark'},
    ]

class Poem(object):
    def GET(self):
        return  json.dumps(data)