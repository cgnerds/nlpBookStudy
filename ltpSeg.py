# -*- coding: utf-8 -*-
import sys
import os
from pyltp import Segmentor

reload(sys)
sys.setdefaultencoding('utf-8')

postdict = {"解 | 空间":"解空间", "深度 | 优先":"深度优先"}

model_path = "../ltp3.4/cws.model"
user_dict = "../ltp3.4/userdict"

segmentor = Segmentor()
#segmentor.load(model_path)
segmentor.load_with_lexicon(model_path, user_dict)

words = segmentor.segment("在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度搜索解空间树。")
seg_sent =  " | ".join(words)
for key in postdict:
    seg_sent = seg_sent.replace(key, postdict[key])
print seg_sent

segmentor.release()