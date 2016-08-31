# -*- coding: utf-8 -*-

import requests
import re
import os
import codecs

def get_title(url):
    s = requests.session()
    h = s.get(url)
    html = h.content.decode('utf-8')
    #print html

    qurl = r'<a href="forum.*? class="s xst">(.*?)</a>'
    qurllist = re.findall(qurl,html)
    #print qurllist


    for each in qurllist:
        f = codecs.open("result.txt", 'a', 'utf-8')
        f.write(each+'\n')
        print each
        #f.flush()
        f.close()

for i in range(1,1000):
    url = 'http://rs.xidian.edu.cn/forum.php?mod=forumdisplay&fid=72&page='+str(i)
    get_title(url)