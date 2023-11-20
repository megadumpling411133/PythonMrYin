# 殷志忠老師(TeacherYin.com)
# set 不重複 無序 項目不可修改 可新增刪除
# https://www.w3schools.com/python/python_sets.asp

import random  # 載入亂數

def 測試1():
    a = {'Tom',100,99}  # 建立集合
    print(type(a))
    print(a)
    a = {'Amy',100,100}  # 建立集合 重複性資料會過濾掉
    print(a)

def 測試2():
    n = random.randint(1,3)  # 亂數範圍 1 ~ 3
    print('n', n)
    if n == 1:
        print('剪刀')
    elif n == 2:
        print('石頭')
    elif n == 3:
        print('布')

def 測試3():
    for i in range(6): # 循環6次
        n = random.randint(1, 42)
        print(f'i={i}  n={n}')

def 測試4():
    a = set()
    for i in range(6):  # 循環6次
        n = random.randint(1, 42)
        print(f'i={i}  n={n}')
        a.add(n)
        print('a', a)
    print('長度', len(a))

def 產生樂透號碼():
    a = set()
    while len(a)<6:  # 資料數量不足6個就循環
        n = random.randint(1, 42)
        a.add(n)
    #print(a)
    b = tuple(a)
    return b

    # 主流程
# 測試1()
# 測試2()
# 測試3()
# 測試4()
c = 產生樂透號碼()
print(type(c))
print(c)