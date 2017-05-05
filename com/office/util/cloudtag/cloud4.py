# -*- coding: utf-8 -*-
import codecs
from com.office.util import fileUtil
from matplotlib.cbook import mkdirs

frequencies = []

fp = codecs.open("rsa_img.txt", "r", 'utf-8');
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
alllines = fp.readlines();

fp.close();
for eachline in alllines:
    line = eachline.split(' ')
    line[1]=int(line[1])
    frequencies.append(line)
    #print eachline,

"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path, removedirs
from wordcloud import WordCloud

import random
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname(__file__)

# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()

# Generate a word cloud image 此处原为 text 方法，我们改用 frequencies 
#wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
imgdir = r"/Users/yangjie/Desktop/moon2.jpg"
import os
dirs,filename = os.path.split(imgdir)
name, ext = os.path.splitext(filename);
destDir = os.path.join(dirs, name);
try:
    removedirs(destDir)
except:
    pass
mkdirs(destDir)
import numpy as np
from PIL import Image
mask = np.array(Image.open(imgdir))
image_colors = ImageColorGenerator(mask)
# take relative word frequencies into account, lower max_font_size
#wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
for scale in range(1,100, 3):
    wordcloud = WordCloud(scale =scale ,mask=mask, font_path='/Users/yangjie/Documents/env/python/simhei.ttf',max_font_size=80, relative_scaling=.5).fit_words(frequencies)
    plt.figure(dpi=100)
    # plt.imshow(wordcloud)
    plt.axis("off")
    plt.imshow(wordcloud.recolor(color_func=image_colors))
#     plt.imshow(wordcloud.recolor(color_func=grey_color_func))
    plt.savefig(destDir + str(r"/result_graf_%d.png"%scale))
#     plt.show()
# The pil way (if you don't have matplotlib)
#image = wordcloud.to_image()
#image.show()
