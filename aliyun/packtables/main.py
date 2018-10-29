#!/usr/bin/python
# encoding=utf8

'''
Created on "2018年8月5日

@author: jyang
'''

if __name__ == '__main__':
    #应用表
    ss = """
    
    {
  "staticpath": "/home/",
  "logoutPage": "/permissions/logout?redirectUrl=",
  "middleware": {
    "login": {
      "enable": false
    },
    "loginLocal": {
      "enable": false
    },
    "aliyunLogin": {
      "enable": false
    },
    "thirdPartyBind": {
      "enable": false
    }
  },
     "apps"desc"":{
    "10001: {
      "name": '警情处置',
      "desc": ''
    },
    "10002: {
      "name": '公众服务',
      "desc": ''
    },
    "10003: {
      "name": '重点车辆',
      "desc": ''
    },
    "10004: {
      "name": '数据监控',
      "desc": ''
    },
    "10005: {
      "name": '云资源平台',
      "desc": ''
    },
    "10006: {
      "name": '权限管理',
      "desc": ''
    },
    "20004: {
      "name": '数据魔方',
      "desc": ''
    },
    "20001: {
      "name": '信号服务平台（银江）',
      "desc": ''
    },
    "20002: {
      "name": '指挥调度（银江）',
      "desc": ''
    },
    "20003: {
      "name": '一路护航',
      "desc": ''
    },

    "20005: {
      "name": '队伍监管',
      "desc": ''
    }
  },
  addApps"desc":{
    "20006: {
      "name": '队伍监管2222',
      "desc": ''
    }
  },
  appsPermissions:{
    "10001": {
      "isShow": false,
      "path": '/event-handle-v2/'
    },
    "10002": {
      "isShow": false,
      "path": '/upps/'
    },
    "10003": {
      "isShow": false,
      "path": '/app/vehicles-monitoring'
    },
    "10004": {
      "isShow": false,
      "path": 'http://33.83.56.44:8080/#/a/a/5'
    },
    "10005": {
      "isShow": false,
      "path": 'http://33.83.56.44:8080/#/a/a/1'
    },
    "10006": {
      "isShow": false,
      "path": '/services/admin/user'
    },
    "20004": {
      "isShow": false,
      "path": 'https://quickbi.hzjjcloud.bj.cn'
    },
    "20001": {
      "isShow": false,
      "path": '/unknown'
    },
    "20002": {
      "isShow": false,
      "path": '/unknown'
    },
    "20003": {
      "isShow": false,
      "path": '/unknown'
    },

    "20005": {
      "isShow": false,
      "path": '/unknown'
    }
  }
}
"""
    print ss.replace("'", '"');
    
    
    