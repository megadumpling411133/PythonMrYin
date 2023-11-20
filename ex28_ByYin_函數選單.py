# 殷志忠老師(TeacherYin.com)

def 顯示選單():
    s = '''
    1. 輸入資料
    2. 打包資料
    3. 儲存資料
    4. 讀取資料
    請選擇: 
    '''
    op = int(input(s))
    if op < 1 or op > 4:
        print('輸入錯誤，沒有這個選項')
    return op

def 輸入資料():
    # 輸入資料
    n = input('輸入 name: ')
    e = int(input('輸入 eng: '))
    m = int(input('輸入 math: '))
    return n,e,m

def 打包資料():
    a = [n,e,m]
    return a

def 儲存():
    print('--- 檔案儲存 st4.txt ---')
    f = open('st4.txt', 'w', encoding='UTF-8')
    s = f'{a[0]} {a[1]} {a[2]}'
    f.write(s)
    f.close()

def 讀取():
    print('--- 檔案讀取 st4.txt ---')
    f = open('st4.txt', 'r', encoding='UTF-8')
    for s in f:
        print(s)
    f.close()

# 主程式
# op = 顯示選單()
# print('op', op)
n,e,m = 輸入資料()
# print(n,e,m)
a = 打包資料()
# print(a)
儲存()
讀取()