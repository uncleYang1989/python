#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年10月12日

@author: Administrator
'''
f1=open("prescription_composition","r").readlines()
f3=open("herb_latin_piyin","r")
f2=open("prescription_composition_eng","a")

for lines in f1:
    newline=""
    lines=lines.split(",")
    lines.pop()
    print lines
    for i in range(len(lines)):
        for herbs in f3:
            herbs=herbs.split("\t")
            print herbs
            if herbs[0].strip()==lines[i].strip():
                newline=newline+herbs[1].strip()+","
                print newline
                break
    f2.write(newline)
                
print "over"