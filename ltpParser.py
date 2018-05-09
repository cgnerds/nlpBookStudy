# -*- coding: utf-8 -*-
import sys
import os
import nltk
from nltk.tree import Tree # 导入 nltk tree 结构
from nltk.grammar import DependencyGrammar # 导入依存句法包
from nltk.parse import *
from pyltp import * # 导入 ltp 应用包
import re

reload(sys)
sys.setdefaultencoding('utf-8') # 设置 UTF-8 输出环境

words = "罗马尼亚 的 首都 是 布加勒斯特 。".split(" ") # 例句

postagger = Postagger() # 首先对句子进行词性标注
postagger.load("../ltp3.4/pos.model")
postags = postagger.postag(words)

parser = Parser() #  将词性标注和分词结果都加入分析器中进行句法解析
parser.load("../ltp3.4/parser.model")
arcs = parser.parse(words, postags)
arclen = len(arcs)
conll = ""
for i in xrange(arclen): # 构建 Conll 标准的数据结构
    if arcs[i].head == 0:
        arcs[i].relation = "ROOT"
    conll += "\t" + words[i] + "(" + postags[i] + ")" + "\t" + postags[i] + "\t" + str(arcs[i].head) + "\t" + arcs[i].relation + "\n"

print conll

conlltree = DependencyGraph(conll) # 转换为依存句法图
tree = conlltree.tree() # 构建树结构
tree.draw() # 显示输出的树