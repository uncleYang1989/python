#!/usr/bin/python
# -*-coding:UTF-8-*-
# encoding=utf8
def do(n):
    l = range(1, n+1);
    index = -1;
    while len(l) > 1:
        for i in range(3):
            index +=1;
            if index >= len(l):
                index = 0;
        l.remove(l[index]);
        index -= 1
        if index == -1:
            index = len(l) -1;
    print u"1.人数为%d时，第%d个人最后留下"%(n, l[0])
    
    
    
def do2(n):
    l = range(1, n+1);
    count = 0;
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
    
    
class Persons():
    def __init__(self, num):
        self.list = range(1, num + 1);
        self.index = -1;
    def remove(self):
        self.list.remove(self.list[self.index])
        self.index -= 1;
    def next(self):
        self.index += 1;
        if self.index == len(self.list):
            self.index = 0
class Boss():
    def __init__(self, num):
        self.persons = Persons(num);
        self.result = -1;
    def start(self):
        status = 1
        while len(self.persons.list) > 1:
            self.persons.next()
            if status == 3:
                self.persons.remove();
                status = 1
            else:
                status += 1;
        self.result = self.persons.list
for n in range(3,10):
    do(n)          
    do2(n)   
    boss = Boss(n);
    boss.start()
    print boss.result 
