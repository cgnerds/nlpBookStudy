# -*- coding: utf-8 -*-
import sys
import os
import jieba # 导入结巴分词库

# 设置 UTF-8 输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

# 结巴分词——全模式
jieba.load_userdict("userdict")
sent = "在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树。"
wordlist = jieba.cut(sent, cut_all=True)
print " | ".join(wordlist)

# 结巴分词——精确切
wordlist = jieba.cut(sent) # cut_all=True
print " | ".join(wordlist)

# 结巴分词——搜索引擎模式
wordlist = jieba.cut_for_search(sent)
print " | ".join(wordlist)
