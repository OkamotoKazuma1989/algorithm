# algorithm
数学的なアルゴリズムを記録

# 基数の変換
n = int(input("数字を入力する:"))
base = int(input("変換したい基数:"))

def convert(n, base):
    result = ""
    
    while n > 0:
        result = str(n % base) + result 
        #nをbaseで割ったあまりを算出
        n //= base
        # nをbaseで割った商を算出

    return result

print(convert(n, base))
