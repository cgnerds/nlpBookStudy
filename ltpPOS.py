# -*- coding: utf-8 -*-
import sys
import os
from pyltp import *

# 设置 UTF-8 输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

model_path = "../ltp3.4/cws.model"
pos_path = "../ltp3.4/pos.model"

sent = "在 包含 问题 的 所有 解 的 解空间树 中 ， 按照 深度优先 搜索 的 策略 ，从 根节点 出发 深度 搜索 解空间树 。"
words = sent.split(" ")
words 
postagger = Postagger() # 实例化词性标注类
postagger.load(pos_path) # 导入词性标注模型
postags = postagger.postag(words)
for word,postag in zip(words, postags):
    print word + "/" + postag,