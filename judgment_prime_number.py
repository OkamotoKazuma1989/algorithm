# coding: UTF-8

# ＜問題＞
# 素数判定するプログラムを作成しないさい。

import math

def get_prime(n):
    if n <= 1:
        return []

    prime = [2]
    limit = int(math.sqrt(n))

    # 奇数のリストを作成（偶数は2で割れるので、ここで除外）
    data = [i + 1 for i in range(2, n, 2)]

    while limit >= data[0]:
        prime.append(data[0])
        # 1.data[0]の奇数（=3）をprimeリストに追加
        # 3.dataリストでdata[0](=3,5,7... <= nの平方根)で全て割れるものを除外したのちdata[0]をprimeリストに追加
        data = [j for j in data if j % data[0] != 0]
        # 2.data[0](=3,5,7... <= nの平方根)で割れない奇数リストを作成（＝data[0]で割れるものはリストから除外）

    return prime + data

print(get_prime(200))

"""
# 割り切れない数だけを取り出す
    for j in deta:
        if j % data[0] != 0:
            deta = [j]

    return prime + deta

print(get_prime(1))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
    # math.sqrtは平方根を返すメソッド
        if n % i == 0:
            return False
    return True

for i in range(200):
    if is_prime(i):
        print(i)
"""
