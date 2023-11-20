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
    global 已輸入  # 聲明使用的全域變數(函數外面的變數 共享的變數)
    # 輸入資料
    n = input('輸入 name: ')
    e = int(input('輸入 eng: '))
    m = int(input('輸入 math: '))
    已輸入 = True
    return n,e,m

def 打包資料():
    #if n is None or e is None or m is None:
    if 已輸入 == False:
        print('打包失敗，資料尚未輸入')
        return  # 函數結束
    a = [n,e,m]
    print('打包資料', a)
    return a


def 儲存_覆蓋():
    global 已儲存  # 聲明使用的全域變數(函數外面的變數 共享的變數)
    print('--- 檔案儲存 覆蓋 st4.txt ---')
    if a is None:
        print('儲存失敗，資料尚未打包')
        return  # 函數結束
    f = open('st4.txt', 'w', encoding='UTF-8')
    s = f'{a[0]} {a[1]} {a[2]}\n'
    f.write(s)
    f.close()
    已儲存 = True
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
    try:
        f = open('st4.txt', 'r', encoding='UTF-8')
        for s in f:
            print(s)
        f.close()
    except FileNotFoundError:
        print('檔案不存在，請先儲存')

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
n,e,m = None,None,None
已輸入 = False
已儲存 = False
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
        if 已輸入 == True and 已儲存 == False:
            x = input('資料輸入尚未儲存，是否要結束 ( y ) ? ')
            if x == 'y':
                break  # 結束迴圈
        else:
            break  # 結束迴圈
print('--- 結束 ---')