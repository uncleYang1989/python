# -*- coding: utf-8 -*-
""""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'rsa_img.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "/Users/yangjie/Downloads/qq/f4f846691ade18c2bfea80b89051cb5d_b (1).jpg")))

wc = WordCloud(font_path='/Users/yangjie/Downloads/chrome/simhei.ttf',background_color="white", max_words=2000, mask=alice_mask,
               stopwords=STOPWORDS.add("said"))
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "/Users/yangjie/Downloads/qq/f4f846691ade18c2bfea80b89051cb5d_b (1).jpg"))

# show
plt.imshow(wc)
# plt.axis("off")
# plt.figure()
# plt.imshow(alice_mask, cmap=plt.cm.gray)
# plt.axis("off")
plt.show()