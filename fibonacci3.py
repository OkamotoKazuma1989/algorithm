# coding: UTF-8

# ＜問題＞
# フィボナッチ数列のプログラムを作成しないさい。

def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-2] + fib[i-1])
    return fib[n - 1]

print(fibonacci(200))