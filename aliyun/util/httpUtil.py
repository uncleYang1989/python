#!/usr/bin/python
# encoding=utf8

def get(url, textmod):
    import urllib, urllib2,json
#     textmod = json.dumps(textmod)
    textmod = urllib.urlencode(textmod)
#     print '%s%s%s' % (url, '?', textmod)
    req = urllib2.Request(url='%s%s%s' % (url, '?', textmod))
    return http(req);


def post(url, textmod):
    import json, urllib2
    textmod = json.dumps(textmod)
#     print textmod
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko', "Content-Type": "application/json"}
    req = urllib2.Request(url=url, data=textmod, headers=header_dict)
    return http(req);

def http(req):
    import urllib2
    try:
        res=urllib2.urlopen(req)
        return res.read();
    except urllib2.HTTPError,e:
        return e.read()


# 输出内容:{"jsonrpc":"2.0","result":"2c42e987811c90e0491f45904a67065d","id":1}
if __name__ == "__main__":
    #http://10.218.135.103:8777/user/ticketCheck?ticket=oQXc4TzR
    url = 'http://10.218.135.103:8777/user/login'
    textmod = {'username':'zhidui_admin_1', 'app_name':'jyang0713', "password":"admin"}
    print post(url, textmod);
