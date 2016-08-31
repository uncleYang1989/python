# -*- coding: utf-8 -*-
import codecs

frequencies = []

fp = codecs.open("ss.txt", "r", 'utf-8');

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

from os import path
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
imgdir = r"/Users/yangjie/Desktop/b999a9014c086e06da825d6403087bf40ad1cbf3.jpg"
import numpy as np
from PIL import Image
mask = np.array(Image.open(imgdir))
# take relative word frequencies into account, lower max_font_size
#wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
wordcloud = WordCloud(mask=mask, font_path='/Users/yangjie/Downloads/chrome/simhei.ttf').fit_words(frequencies)
plt.figure(dpi=800)
plt.axis("off")
plt.imshow(wordcloud.recolor(color_func=grey_color_func, random_state=3))
plt.savefig("result4.png")
# plt.show()
# The pil way (if you don't have matplotlib)
