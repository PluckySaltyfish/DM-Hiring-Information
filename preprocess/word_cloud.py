#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import fm
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud, ImageColorGenerator

# import matplotlib.mlab as mlab

font = FontProperties(fname='Songti.ttc')
bar_width = 0.5
lyric = ''

# jieba.analyse.set_stop_words("stop_words.txt")
stop_words = set(fm.load_file('stop_words.txt'))

seg_words = fm.load_file('seg_words.txt')
text = ' '.join(str(seg) for seg in seg_words)
# result = jieba.analyse.textrank(lyric, topK=50, withWeight=True)

# keywords = dict()
# for i in result:
#     keywords[i[0]] = i[1]
# print(keywords)

image = Image.open('./background.png')
graph = np.array(image)
wc = WordCloud(font_path='Songti.ttc', background_color='White', max_words=50, mask=graph, stopwords=stop_words, collocations=False)
wc.generate(text)
image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()
wc.to_file('output.png')

X = []
Y = []


num = len(X)

fig = plt.figure(figsize=(28, 10))
plt.bar(range(num), Y, tick_label=X, width=bar_width)
# plt.xlabel("X-axis",fontproperties=font)
# plt.ylabel("Y-axis",fontproperties=font)
plt.xticks(rotation=50, fontproperties=font, fontsize=20)
plt.yticks(fontsize=20)
plt.title("words-frequency chart", fontproperties=font, fontsize=30)
plt.savefig("barChart.jpg", dpi=360)
plt.show()