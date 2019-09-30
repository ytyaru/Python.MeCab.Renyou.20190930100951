#!/usr/bin/env python3
# coding: utf8
import Precaution
import Renyou
#import Mizen

def prints(words):
    for word in words:
        if word is not None: print(word)
def get_mizens(row):
    return (mizen.get_not(row),
            mizen.get_not_old(row),
            mizen.get_conn(row),
            mizen.get_not_special(row),
            mizen.get_reru(row))
def get_renyous(row):
    return (renyo.get_howto(row),
            renyo.get_state(row),
            renyo.get_start(row),
            renyo.get_end(row),
            renyo.get_conn(row))

p = Precaution.Precaution()
#mizen = Mizen.Mizen()
renyo = Renyou.Renyou()
words = ['走る','押す','愛する','見る','食べる','来る','悲しい','ござる']
for word in words:
    print('===== {} ====='.format(word))
    rows = p.get(word)
    for row in rows:
        prints(get_renyous(row))
"""
定まる,772,772,6852,動詞,自立,*,*,五段・ラ行,基本形,定まる,サダマル,サダマル

0: 語(word)
1,2,3:
4: 品詞(word_class)
5: 単語種別(word_type)
6,7:
8: 活用種別(conj_type) 
9: 活用形種別(conj)
10: 語の基本形(word_base)
11,12: 読み？発音？
"""
