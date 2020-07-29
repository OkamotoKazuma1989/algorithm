# coding: UTF-8

# ＜問題＞
# 1から100までの数を順に出力するプログラムを作成しなさい。
# ただし、3の倍数のときは数の代わりに「Fizz」を、5の倍数のときは「Buzz」を、3と5の両方の倍数の場合には
# 「FizzBuzz」を出力するものとする

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
