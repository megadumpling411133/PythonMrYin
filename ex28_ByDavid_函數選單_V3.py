# 殷志忠老師(TeacherYin.com)

# def 顯示選單():
#     s = '''
#     1. 輸入資料
#     2. 打包資料
#     3. 儲存資料
#     4. 讀取資料
#     5. 結束
#     請選擇:
#     '''
#     try:
#         op = int(input(s))
#         if op < 1 or op > 5:
#             print('輸入錯誤，沒有這個選項')
#         return op
#     except ValueError:
#         print('輸入格式錯誤，請輸入數字')
def 選擇選項():
    s = '''動作選單:
        0. 輸入檔名
        1. 輸入資料
        2. 打包資料
        3. 儲存資料
        4. 讀取資料
        9. 結束操作'''
    while True :
        # 檢查錯誤
        try:
            # 檢查動作編號範圍 1 ~ 5
            while True:
                op = int(input(f'{s}\n請選擇執行動作: '))
                if (0 <= op <= 4) or op == 9:
                    if op == 0:
                        action = f"輸入檔名: {op}"
                    elif op == 1:
                        action = "輸入資料"
                    elif op == 2:
                        action = "打包資料"
                    elif op == 3:
                        action = "儲存資料"
                    elif op == 4:
                        action = "讀取資料"
                    elif op == 9:
                        action = "結束操作"
                    print(f"目前選擇動作: {op}. {action}")
                    return op
                else:
                    print("請輸入選項範圍: 動作(1 ~ 4) 或是 結束(9) \n請重新輸入")
        # 檢查整數輸入錯誤
        except ValueError:
            print("輸入錯誤，請輸入整數數字")
        # 檢查其他錯誤
        except Exception as err:
            print(f'發生其他錯誤: {err} !!!')

# def 輸入資料():
#     global 已輸入  # 聲明使用的全域變數(函數外面的變數 共享的變數)
#     # 輸入資料
#     n = input('輸入 name: ')
#     e = int(input('輸入 eng: '))
#     m = int(input('輸入 math: '))
#     已輸入 = True
#     return n,e,m
# def 檢查分數(CheckPoint):
#     for i in CheckPoint:
#         if 0 <= int(i) <= 100:
#             # 打包資料 > 寫成另一支 function
#             # Dlist = [n, e, m]
#             # return Dlist
#             return True
#         else:
#             print("請輸入介於 0 ~ 100 的分數!")
#             break
def 檢查分數(CheckPoint):
    for e in CheckPoint:
        if 0 <= e <= 100:
            # 打包資料 > 寫成另一支 function
            # Dlist = [n, e, m]
            # return Dlist
            return
            # for m in CheckPoint:
            #     if 0 <= m <= 100:
            #         return
            #     else:
            #         print("請輸入介於 0 ~ 100 的分數!")
            #         break
        else:
            print("請輸入介於 0 ~ 100 的分數!")
            break
def 輸入資料():
    while True:
        try:
            n = input('Please sign your name here: ')
            e = int(input('Please enter your english score here: '))
            CheckPoint = [e]
            檢查分數(CheckPoint)
            m = int(input('Please enter your math score here: '))
            CheckPoint = [m]
            檢查分數(CheckPoint)
            return n, e, m
            # CheckPoint = [e, m]
            # if 檢查分數(CheckPoint):
            #     if 檢查分數(CheckPoint):
            #         return n, e, m
        # 檢查整數輸入錯誤
        except ValueError:
            print("輸入錯誤，請輸入整數成績")
        # 檢查其他錯誤
        except Exception as err:
            print(f'發生其他錯誤: {err} !!!')
def 打包資料():
    #if n is None or e is None or m is None:
    if 已輸入 == False:
        print('打包失敗，資料尚未輸入')
        return  # 函數結束
    package = [n,e,m]
    print('打包資料', package)
    return package


def 儲存_覆蓋():
    global 已儲存  # 聲明使用的全域變數(函數外面的變數 共享的變數)
    print('--- 檔案儲存 覆蓋 st4.txt ---')
    if package is None:
        print('儲存失敗，資料尚未打包')
        return  # 函數結束
    f = open('st4.txt', 'w', encoding='UTF-8')
    s = f'{package[0]} {package[1]} {package[2]}\n'
    f.write(s)
    f.close()
    已儲存 = True
    print('儲存成功')

def 儲存_附加():
    print('--- 檔案儲存 附加 st4.txt ---')
    if package is None:
        print('儲存失敗，資料尚未打包')
        return  # 函數結束
    f = open('st4.txt', 'a', encoding='UTF-8')
    s = f'{package[0]} {package[1]} {package[2]}\n'
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


package = None   # 尚未打包
n,e,m = None,None,None
已輸入 = False
已儲存 = False
while True:
    # a = None
    op = 選擇選項()
    if op == 1:
        n, e, m = 輸入資料()
    elif op == 2:
        package = 打包資料()
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