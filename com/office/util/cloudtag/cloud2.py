# -*- coding: utf-8 -*-
import codecs

frequencies = []

fp = codecs.open("rsa.txt", "r", 'utf-8');

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

d = path.dirname(__file__)

# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()

# Generate a word cloud image 此处原为 text 方法，我们改用 frequencies 
#wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt

# take relative word frequencies into account, lower max_font_size
#wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
wordcloud = WordCloud(font_path='/Users/yangjie/Documents/env/python/simhei.ttf',max_font_size=80, relative_scaling=.5).fit_words(frequencies)
plt.figure(dpi=1800)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("result.png")

# The pil way (if you don't have matplotlib)
#image = wordcloud.to_image()
#image.show()
