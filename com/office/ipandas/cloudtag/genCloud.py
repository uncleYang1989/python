# -*- coding: utf-8 -*-
import codecs
import random
from pytagcloud import create_tag_image, make_tags, \
    LAYOUT_HORIZONTAL
from pytagcloud.colors import COLOR_SCHEMES

wd = {}

fp=codecs.open("rsa.txt", "r",'utf-8');

alllines=fp.readlines();

fp.close();

for eachline in alllines:
    line = eachline.split('        ')
    #print eachline,
    wd[line[0]] = int(line[1])
print wd


from operator import itemgetter
swd = sorted(wd.iteritems(), key=itemgetter(1), reverse=True)
tags = make_tags(swd,minsize = 50, maxsize = 240,colors=random.choice(COLOR_SCHEMES.values()))
create_tag_image(tags, 'keyword_tag_cloud4.png', background=(0, 0, 0, 255),
size=(2400, 1000),layout=LAYOUT_HORIZONTAL,
fontname="SimHei")