# -*- coding: utf-8 -*-
import sys
import os
from pyltp import *

# 设置 UTF-8 输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

MODELDIR = "../ltp3.4/"
sentence = "欧洲东部的罗马尼亚，首都是布加勒斯特，也是一座世界性的城市。"
segmentor = Segmentor()
segmentor.load(os.path.join(MODELDIR, "cws.model"))
words = segmentor.segment(sentence)
wordlist = list(words) # 从生成器变为列表元素

postagger = Postagger()
postagger.load(os.path.join(MODELDIR, "pos.model"))
postags = postagger.postag(words)

parser = Parser()
parser.load(os.path.join(MODELDIR, "parser.model"))
arcs = parser.parse(words, postags)

recognizer = NamedEntityRecognizer()
recognizer.load(os.path.join(MODELDIR, "ner.model"))
netags = recognizer.recognize(words, postags)

# 语义角色标注
labeller = SementicRoleLabeller()
labeller.load(os.path.join(MODELDIR, "pisrl.model"))
roles = labeller.label(words, postags, arcs)

# 输出标注结果
for role in roles:
    print 'rel: ', wordlist[role.index] # 谓词
    for arg in role.arguments:
        if arg.range.start != arg.range.end:
            print arg.name, ' '.join(wordlist[arg.range.start:arg.range.end])
        else:
            print arg.name, wordlist[arg.range.start]