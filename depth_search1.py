# coding: UTF-8

# ＜問題＞
# 深さ優先探索（行きがけ）のプログラムを作成しなさい。

tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]

def search(pos):
    print(pos)
    #配下のノード（節点）を調べる前の出力
    for i in tree[pos]:
    #配下のノード（節点）を調べる
        search(i)
        #再帰的に探索

search(0)
