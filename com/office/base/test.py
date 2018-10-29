#!/usr/bin/python
# encoding=utf8

def sortset(ss):
    funcs = set(ss.replace("\n", "sp").strip().split("sp"))
    for f in funcs:
        if f:
            print f
             
sortset("""实时处置
消息推送、查看
大队界面切换
事件查询
自定义区域划分
阈值管理
操作日志查询
统计分析
实时处置
消息推送、查看
大队界面切换
事件查询
自定义区域划分
操作日志查询
统计分析
实时处置
事件查询
自定义区域划分
操作日志查询
统计分析""")