#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
def readDocx(docName):
    fullText = []
    import docx
    doc = docx.Document(docName)
    paras = doc.paragraphs
    for p in paras:
        fullText.append(p.text)
    return '\n'.join(fullText)

if __name__ == "__main__":
    content = readDocx("/Users/yangjie/Downloads/qq/(最完整版)胡希恕讲伤寒论.docx")
    lines = content.split(u"。")
    for line in lines:
        print line
