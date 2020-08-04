# coding: UTF-8

# ＜問題＞
# ハノイの塔問題のプログラムを作成しなさい。

def hanoi(n,src,dist,via):#src:移動元,dist:移動先,via:経由場所
    if n > 1:
        hanoi(n - 1, src , via, dist)#n-1枚を移動元から経由場所を移す
        print(src + " -> " +  dist)
        hanoi(n - 1, via , dist, src)#n-1枚を経由場所から移動先を移す
    else:
        print(src + " -> " +  dist)

n = int(input())
hanoi(n,"a","b","c")
