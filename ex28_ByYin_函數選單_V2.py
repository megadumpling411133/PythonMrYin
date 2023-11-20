# 殷志忠老師(TeacherYin.com)

def 顯示選單():
    s = '''
    1. 輸入資料
    2. 打包資料
    3. 儲存資料
    4. 讀取資料
    5. 結束
    請選擇: 
    '''
    try:
        op = int(input(s))
        if op < 1 or op > 5:
            print('輸入錯誤，沒有這個選項')
        return op
    except ValueError:
        print('輸入格式錯誤，請輸入數字')

def 輸入資料():
    # 輸入資料
    n = input('輸入 name: ')
    e = int(input('輸入 eng: '))
    m = int(input('輸入 math: '))
    return n,e,m

def 打包資料():
    a = [n,e,m]
    print('打包資料', a)
    return a

def 儲存_覆蓋():
    print('--- 檔案儲存 覆蓋 st4.txt ---')
    if a is None:
        print('儲存失敗，資料尚未打包')
        return  # 函數結束
    f = open('st4.txt', 'w', encoding='UTF-8')
    s = f'{a[0]} {a[1]} {a[2]}\n'
    f.write(s)
    f.close()
    print('儲存成功')

def 儲存_附加():
    print('--- 檔案儲存 附加 st4.txt ---')
    if a is None:
        print('儲存失敗，資料尚未打包')
        return  # 函數結束
    f = open('st4.txt', 'a', encoding='UTF-8')
    s = f'{a[0]} {a[1]} {a[2]}\n'
    f.write(s)
    f.close()
    print('儲存成功')
def 讀取():
    print('--- 檔案讀取 st4.txt ---')
    f = open('st4.txt', 'r', encoding='UTF-8')
    for s in f:
        print(s)
    f.close()

# def 執行選項():
#     if op == 1:
#         n, e, m = 輸入資料()
#     elif op == 2:
#         a = 打包資料()
#     elif op == 3:
#         儲存()
#     elif op == 4:
#         讀取()

# 主程式
# op = 顯示選單()
# print('op', op)
# n,e,m = 輸入資料()
# print(n,e,m)
# a = 打包資料()
# print(a)
# 儲存()
# 讀取()
a = None   # 尚未打包
while True:
    # a = None
    op = 顯示選單()
    if op == 1:
        n, e, m = 輸入資料()
    elif op == 2:
        a = 打包資料()
    elif op == 3:
        儲存_覆蓋()
    elif op == 4:
        讀取()
    elif op == 5:
        break  # 結束迴圈
print('--- 結束 ---')