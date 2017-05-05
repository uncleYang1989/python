# -*- coding: utf-8 -*-
import sys
from com.office.util.codeUtil import forbidCodeErr
forbidCodeErr()
from com.office.util.fileUtil import writeFile, readFile
sys.path.append('../')

import jieba.analyse

# file_name = "/Users/yangjie/Downloads/chrome/511.txt"
topK = 1000;
withWeight = True;
import codecs
# fp = codecs.open("/Users/yangjie/Downloads/qq/新建文本文档.txt", "r", 'gbk');
# 
# alllines = fp.readlines();
# content = ""
# for line in alllines:
#     content += line
content = readFile("tmp.txt");
writeFile("tmp2.txt", content);
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)

result = ""
if withWeight is True:
    for tag in tags:
        if  tag[0] in [u"杨大爷", u"孔敏佳"]:
            continue
        result += tag[0]
        result += " "
        result += str(int(tag[1]*1000))
        result += "\n"
        print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
else:
    print(",".join(tags))
writeFile("rsa_img.txt", result)