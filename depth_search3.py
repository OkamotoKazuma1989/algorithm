# coding: UTF-8

# ＜問題＞
# 深さ優先探索（通りがけ）のプログラムを作成しなさい。

tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]

def search(pos):
    if len(tree[pos]) == 2:
    #子が2つあるとき
        search(tree[pos][0])
        print(pos)
        #左のノード（節点）と右のノードの間に出力
        search(tree[pos][1])
    elif len(tree[pos]) == 1:
        search(tree[pos][0])
        print(pos)
        #左のノード（節点）を調べた後に出力
    else:
    #配下のノード（節点）がないとき
        print(pos)

search(0)
