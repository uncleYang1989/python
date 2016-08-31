#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8

'''
【程序37】 
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下
的是原来第几号的那位。 
'''

def do2(n):
    l = range(1, n+1);
    count = 1;
    while len(l) > 1:
        removeList = []
        for i in l:
            count +=1
            if count == 3:
                removeList.append(i)
                count=0
        for i in removeList:
            l.remove(i)
    print u"2.人数为%d时，第%d个人最后留下"%(n, l[0])
for n in range(3,10):
    do2(n)    
    
'''
2.人数为3时，第2个人最后留下
2.人数为4时，第1个人最后留下
2.人数为5时，第4个人最后留下
2.人数为6时，第1个人最后留下
2.人数为7时，第4个人最后留下
2.人数为8时，第7个人最后留下
2.人数为9时，第1个人最后留下
'''