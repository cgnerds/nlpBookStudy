# -*- coding: utf-8 -*-
import sys
import os
from stanford import StanfordPOSTagger

# 设置 UTF-8 输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

root = '../stanford-corenlp/'
jarpath = root + "stanford-postagger.jar"
modelpath = root + "models/pos-tagger/chinese-distsim/chinese-distsim.tagger"

st = StanfordPOSTagger(jarpath, modelpath)
seg_sent = "在 包含 问题 的 所有 解 的 解空间树 中 ， 按照 深度优先 搜索 的 策略 ，从 根节点 出发 深度 搜索 解空间树 。"
postest = "postest"
result = "result"
taglist = st.tag(seg_sent)
print taglist