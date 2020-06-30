#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import pandas as pd
from preprocess import fm
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from wordcloud import WordCloud, ImageColorGenerator


font = FontProperties(fname='Songti.ttc')


def generate_word_cloud(seg_words, res_path):
    stop_words = set(fm.load_file('segment/result/stop_words.txt'))
    text = ' '.join(str(seg) for seg in seg_words)
    image = Image.open('word_cloud/background.png')
    graph = np.array(image)
    wc = WordCloud(font_path='word_cloud/Songti.ttc', background_color='White', max_words=50, mask=graph,
                   stopwords=stop_words, collocations=False)
    wc.generate(text)
    image_color = ImageColorGenerator(graph)
    plt.imshow(wc)
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    plt.show()
    wc.to_file(res_path)


if __name__ == '__main__':
    df = pd.read_csv('../data/去噪声后数据.csv')
    segment_words = df['welfare'].dropna().to_list()
    generate_word_cloud(segment_words, 'word_cloud/result/welfare.png')
    segment_words = fm.load_file('segment/result/seg_words.txt')
    generate_word_cloud(segment_words, 'word_cloud/result/description.png')
