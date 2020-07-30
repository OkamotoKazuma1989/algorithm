# coding: UTF-8

# ＜問題＞
# 2進数から10進数に変換するプログラムを作成しないさい。

input_binary = input("10進数に変換したい2進数を入力してください:")
result = 0

for i in range(len(input_binary)):
    result = result + int(input_binary[i]) * (2 ** (len(input_binary) -i -1))

print(result)
