# coding: UTF-8

# ＜問題＞
# 10進数からn進数に変換するプログラムを作成しないさい。


input_radix = int(input("何進数に変換したいですか？:"))
input_decimal = int(input("変換したい自然数を入力してください:"))

result = ""
# 変換後の文字列を代入する変数

while input_decimal > 0:
    result = str(input_decimal % input_radix) + result
    # 数字が決まる
    input_decimal = input_decimal // input_radix
    # 桁数が決まる

print(result)
