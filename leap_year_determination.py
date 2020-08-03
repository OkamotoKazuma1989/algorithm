# coding: UTF-8

# ＜問題＞
# 閏年を判定するプログラムを作成しないさい。

start_year = int(input("開始年は？："))
end_year = int(input("終了年は？："))

for i in range(start_year,end_year):
    if i % 4 == 0 and not (i % 100 == 0 and i % 400 != 0):
        result = i
        print(result)
