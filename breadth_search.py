# coding: UTF-8

# ＜問題＞
# 幅優先探索のプログラムを作成しなさい。

tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]
data  = [0]

while len(data) > 0:
    pos = data.pop(0)
    #先頭からデータを取り出す
    print(pos)
    for i in tree[pos]:
        data.append(i)
        #末尾に追加
