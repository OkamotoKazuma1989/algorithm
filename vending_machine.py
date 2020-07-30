# coding: UTF-8

# ＜問題＞
# お釣りを計算するプログラムを作成しなさい。
# ただし、お釣りは紙幣・硬貨の枚数が最小となるようにするものとする。


# エラー時に強制終了するためのモジュール
import sys

input_price = input("insert:")
if not input_price.isdecimal():
    print("整数を入力してください")
    sys.exit()
# メモ：文字列中の全ての文字が十進数字で、かつ 1 文字以上あるなら True を、そうでなければ False

product_price = input("product:")
if not product_price.isdecimal():
    print("整数を入力してください")
    sys.exit()

change = int(input_price) - int(product_price)

if change < 0:
    print("金額が不足しています")
    sys.exit()

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change = change % i
    print(str(i) + ": " + str(r))
