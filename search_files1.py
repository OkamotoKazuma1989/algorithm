# coding: UTF-8

# ＜問題＞
# 深さ優先探索でファイルを探すのプログラムを作成しなさい。

import os

def search(dir, name):
    for i in os.listdir(dir):
        if i == name:
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                search(dir + i + "/", name)

search("/","book")
