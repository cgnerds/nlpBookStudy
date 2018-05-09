# -*- coding: utf-8 -*-
import sys
import os

# CoreNLP 3.9.1 jar 包和中文模板包
class StanfordCoreNLP(): # 所有 StanfordNLP的父类
    def __init__(self, jarpath, modelpath):
        self.tempsrcpath = "tempsrc" # 输入临时文件路径
        self.jarpath = jarpath
        self.modelpath = modelpath

    def savefile(self, path, sent): # 创建临时文件存储路径
        fp = open(path, "wb")
        fp.write(sent)
        fp.close()
    
    def delfile(self, path): # 删除临时文件
        os.remove(path)
    
class StanfordPOSTagger(StanfordCoreNLP): # 词性标注子类
    def __init__(self, jarpath, modelpath):
        StanfordCoreNLP.__init__(self, jarpath, modelpath)
        self.classfier = "edu.stanford.nlp.tagger.maxent.MaxentTagger" # 词性标注主类
        self.delimiter = "/" # 标签分隔符
        self.__buildcmd()
    
    def __buildcmd(self): # 构建命令行
        self.cmdline = 'java -mx1g -cp "' + self.jarpath + '" ' + self.classfier + ' -model "' + self.modelpath + '" -tagSeparator ' + self.delimiter
        print self.cmdline

    def tag(self, sent): # 标注句子
        self.savefile(self.tempsrcpath, sent)
        tagtxt = os.popen(self.cmdline + " -textFile " + self.tempsrcpath, 'r').read() # 结果输出到变量中
        self.delfile(self.tempsrcpath)
        return tagtxt
    
    def tagfile(self, inputpath, outpath): # 标注文件
        os.system(self.cmdline + ' -textFile ' + inputpath + ' > ' + outpath)

class StanfordNERTagger(StanfordCoreNLP):
    def __init__(self, jarpath, modelpath):
        StanfordCoreNLP.__init__(self, jarpath, modelpath)
        self.classifier = "edu.stanford.nlp.ie.crf.CRFClassifier"
        self.__buildcmd()
    
    # 构建命令行
    def __buildcmd(self):
        self.cmdline = 'java -mx1g -cp "' + self.jarpath + '" ' + self.classifier + ' -loadClassifier "' + self.modelpath + '"'
        print self.cmdline
    
    # 标注句子
    def tag(self, sent):
        self.savefile(self.tempsrcpath, sent)
        tagtxt = os.popen(self.cmdline + ' -textFile ' + self.tempsrcpath, 'r').read() # 输出到变量中
        self.delfile(self.tempsrcpath)
        return tagtxt
    
    # 标注文件
    def tagfile(self, sent, outpath):
        self.savefile(self.tempsrcpath, sent)
        os.system(self.cmdline + ' -textFile ' + self.tempsrcpath + ' > ' + outpath )
        self.delfile(self.tempsrcpath)

class StanfordParser(StanfordCoreNLP):
    def __init__(self, modelpath, jarpath, opttype):
        StanfordCoreNLP.__init__(self, jarpath, modelpath)
        self.modelpath = modelpath # 模型文件路径
        self.classifier = "edu.stanford.nlp.parser.lexparser.LexicalizedParser"
        self.opttype = opttype
        self.__buildcmd()
    
    # 构建命令行
    def __buildcmd(self):
        self.cmdline = 'java -mx500m -cp "' + self.jarpath + '" ' + self.classifier + ' -outputFormat "' + self.opttype + '" ' + self.modelpath + ' '
        print self.cmdline
    
    # 解析句子
    def parse(self, sent):
        self.savefile(self.tempsrcpath, sent)
        tagtxt = os.popen(self.cmdline + self.tempsrcpath, "r").read() # 输出到变量中
        self.delfile(self.tempsrcpath)
        return tagtxt
    
    # 输出到文件
    def tagfile(self, sent, outpath):
        self.savefile(self.tempsrcpath, sent)
        os.system(self.cmdline + self.tempsrcpath + ' > ' + outpath )
        self.delfile(self.tempsrcpath) 