# coding: UTF-8

# ＜問題＞
# 西暦を和暦に変換するプログラムを作成しないさい。

western_cal = int(input("西暦を入力してください："))

def convert_wtoj(cal):

    meiji = 1868
    taisyo = 1912
    syowa = 1926
    heisei = 1989
    reiwa = 2019

    if cal >= meiji and cal < taisyo:
        japanese_cal = cal - meiji +1
        return print("明治"+str(japanese_cal)+"年")
    elif cal >= taisyo and cal < syowa:
        japanese_cal = cal - taisyo +1
        return print("大正"+str(japanese_cal)+"年")
    elif cal >= syowa and cal < heisei:
        japanese_cal = cal - syowa +1
        return print("昭和"+str(japanese_cal)+"年")
    elif cal >= heisei and cal < reiwa:
        japanese_cal = cal - heisei +1
        return print("平成"+str(japanese_cal)+"年")
    elif cal >= reiwa:
        japanese_cal = cal - reiwa +1
        return print("令和"+str(japanese_cal)+"年")
    else:
        japanese_cal = "変換できません"
        return print(japanese_cal)

convert_wtoj(western_cal)
