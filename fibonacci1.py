# coding: UTF-8

# ＜問題＞
# フィボナッチ数列のプログラムを作成しないさい。

def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(6))
