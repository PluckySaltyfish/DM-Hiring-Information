# -*- coding: utf8 -*-
import json
import fm
import pandas as pd
import requests

request_obj = {
    'str': '',
    'options':
        {
            'input_spec': {'lang': 'auto'},
            'word_seg': {'enable': True},
            'pos_tagging': {'enable': False},
            'ner': {'enable': False},
            'syntactic_parsing': {'enable': False},
            'srl': {'enable': False}
        },
}

request_obj_lst = {
    'str': [],
    'options':
        {
            'input_spec': {'lang': 'auto'},
            'word_seg': {'enable': True},
            'pos_tagging': {'enable': False},
            'ner': {'enable': False},
            'syntactic_parsing': {'enable': False},
            'srl': {'enable': False}
        },
}


def add_sentence_to_request_obj_lst(sent):
    request_obj_lst['str'].append(sent)


def generate_segment_lst_info(res_lst):
    lst = []
    words_lst = []
    for obj in res_lst:
        seg_sent, seg_words_lst = generate_segment_info(obj)
        lst.append(seg_sent)
        words_lst += seg_words_lst
    return lst, words_lst


def request_texSmart(obj):
    req_str = json.dumps(obj).encode()
    url = 'https://texsmart.qq.com/api'
    r = requests.post(url, data=req_str)
    r.encoding = 'utf-8'
    return json.loads(r.text)


def add_sentence_to_request_obj(sent):
    request_obj['str'] = sent


def generate_segment_info(obj):
    seg_sent = [seg_obj['str'] for seg_obj in obj['phrase_list']]
    return ','.join(str(seg) for seg in seg_sent), seg_sent


if __name__ == '__main__':
    df = pd.read_csv('../../data/去噪声后数据.csv')
    lst = []
    seg_words = []
    for i in range(len(df)):
        add_sentence_to_request_obj(df.loc[i, 'description'])
        try:
            seg_description, seg_lst = generate_segment_info(request_texSmart(request_obj))
            df.loc[i, 'description'] = seg_description
            seg_words += seg_lst
        except Exception:
            lst.append(str(i))
    fm.save_file('result/seg_words.txt', seg_words)
    fm.save_file('result/exception.txt', lst)
    df.to_csv('../data/segment.csv')
