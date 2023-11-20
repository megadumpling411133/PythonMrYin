# 導入 random 模組
import random

def T1():
    # 建立 set
    a = {'David', 100, 99}
    print(type(a))
    print(a)
    # set 會過濾重複值
    a = {'Davies', 100, 100}
    print(a)

# random 從 1 開始
def T2():
    n = random.randint(1, 3) # 隨機整數 1 ~ 3
    if n == 1:
        print("剪刀")
    elif n == 2:
        print('石頭')
    elif n == 3:
        print('布')

# 直接使用隨機整數做樂透 可能會抽出重複號碼
def T3():
    for i in range(6):
        n = random.randint(1, 42) # 隨機整數 1~ 42
        print(f'隨機取號第 {i} 抽, 抽到值為: {n}')

# 用 set 去除重複 但發生重複時會等同少抽
def T4():
    s1 = set()
    for i in range(6):  # 抽取 6 次
        n = random.randint(1, 42) # 亂數範圍 1 ~ 42
        print(f'隨機取號第 {i} 抽, 抽到數字為: {n}')
        s1.add(n)
        print(f'S1: {s1}')
    print(f'長度: {len(s1)}')

# 產生樂透號碼 產生候用 tuple 裝箱(packing)
def genNum_lottery():
    s1 = set()
    while len(s1) < 6:  # 抽取出 6 次為止，不足就重抽
        n = random.randint(1, 42)  # 亂數範圍 1 ~ 42
        s1.add(n)
        # print(f'S1: {s1}')
        # print(f'長度: {len(s1)}')
    # 已抽出樂透號碼 但 set 無序 不可改
    t1 = tuple(s1)
    return t1
# T1()
# T2()
# T3()
# T4()
lot_Nug = genNum_lottery()
print(type(lot_Nug))
print(f'lottery Number is: {lot_Nug}')