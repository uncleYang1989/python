#!/usr/bin/python
#-*-coding:UTF-8-*-
# encoding=utf8
'''
Created on 2016年6月20日

@author: yangjie
'''

if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect("ios.db")
    
    conn.execute('DROP TABLE IF EXISTS "keys";')
    conn.execute('''CREATE TABLE "keys" (
     "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
     "keyword" text NOT NULL,
     "status" integer NOT NULL
);''')
    conn.execute('''DROP TABLE IF EXISTS "result";''')
    conn.execute('''CREATE TABLE "result" (
     "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     "first" TEXT,
     "second" TEXT,
     "third" TEXT
);''')

