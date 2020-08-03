# coding: UTF-8

# ＜問題＞
# 二分探索のプログラムを作成しなさい。

def binary_search(data, value):
    left = 0
    #探索する範囲の左端を設定
    right = len(data)-1
    #探索する範囲の右端を設定

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        #中央値と一致した場合は位置を返す
        elif data[mid] < value:
            left = mid + 1
        #中央の値より大きい場合は探索範囲を左に変える
        else:
            right = mid - 1
        #中央の値より小さい場合は探索範囲を左に変える
    return -1

data = [10,20,30,40,50,60,70,80,90]
print(binary_search(data,90))
