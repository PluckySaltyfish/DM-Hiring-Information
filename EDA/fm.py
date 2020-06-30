# -*- coding:utf-8 -*-
import json
import os
import xml.etree.ElementTree as ET


def load_file(filepath, ):
    with open(filepath, encoding='utf-8') as f:
        a = []
        for i in f:
            a.append(i.strip(' \n'))
        return a


def load_dict_json(filepath, ):
    with open(filepath, encoding='utf-8') as f:
        a = json.load(f)
    return a


def save_file(filepath, lst):
    with open(filepath, 'w', encoding='utf-8') as f:
        for i in range(len(lst)):
            f.write(lst[i])
            if i != len(lst) - 1:
                f.write('\n')


def save_dict_json(filepath, dic):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(json.dumps(dic, ensure_ascii=False))


def load_xml(filepath):
    tree = ET.ElementTree()
    tree = ET.parse(filepath)
    children = tree.findall('DOC')
    a = []
    for i in children:
        for j in i[0]:
            a.append(j.text)
    return a


def get_filelist(dir, Filelist):
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
        # 只返回文件名
        # Filelist.append(os.path.basename(dir))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 若需要忽略文件夹
            # if s == "xxx":
            # continue
            newDir = os.path.join(dir, s)
            get_filelist(newDir, Filelist)
    return Filelist


def get_dir_list(dir_path):
    lst = []
    for s in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, s)):
            lst.append(s)
    return lst


if __name__ == '__main__':
    a = load_xml('/Users/plucky/Downloads/tizh/test/ti.xml')
    a = 4 * a
    print(len(a))

    save_file('/Users/plucky/Downloads/tizh/test/test.src', a)
    b = load_xml('/Users/plucky/Downloads/tizh/test/zh.xml')
    print(len(b))
    save_file('/Users/plucky/Downloads/tizh/test/test.trg', b)
