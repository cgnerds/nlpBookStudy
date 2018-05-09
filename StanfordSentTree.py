# -*- coding: utf-8 -*- 
import sys
import os
from nltk.tree import Tree # 导入 NLTK 库
from stanford import *

# 设置 UTF-8 输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

# 安装库
root = '../stanford-corenlp/'
jarpath = root + "stanford-parser.jar"
modelpath = root + "models/lexparser/chinesePCFG.ser.gz"
opttype = 'penn' # 宾州树库格式
parser = StanfordParser(modelpath, jarpath, opttype)
result = parser.parse("罗马尼亚 的 首都 是 布加勒斯特 。")
print result
tree = Tree.fromstring(result)
tree.draw()