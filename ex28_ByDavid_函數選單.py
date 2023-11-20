def 選擇選項():
    s = '''動作選單:
        1. 輸入資料
        2. 打包資料
        3. 儲存資料
        4. 讀取資料'''
    while True :
        # 檢查錯誤
        try:
            # 檢查動作編號範圍 1 ~ 4
            while True:
                op = int(input(f'{s}\n請選擇執行動作: '))
                if 0 < op <= 4:
                    if op == 1:
                        action = "輸入資料"
                    elif op == 2:
                        action = "打包資料"
                    elif op == 3:
                        action = "儲存資料"
                    elif op == 4:
                        action = "讀取資料"
                    print(f"目前選擇動作: {op}. {action}")
                    return op
                else:
                    print("請輸入選項範圍: 1 ~ 4 \n請重新輸入")
        # 檢查整數輸入錯誤
        except ValueError:
            print("輸入錯誤，請輸入整數數字")
        # 檢查其他錯誤
        except Exception as err:
            print(f'發生其他錯誤: {err} !!!')
# def 檢查成績_hide(score):
#     while True:
#         if 0 <= score <= 100:
#             # 打包資料 > 寫成另一支 function
#             # Dlist = [n, e, m]
#             # return Dlist
#             break
#         else:
#             print("請輸入介於 0 ~ 100 的分數!")
#         return score
#
# def 輸入資料_hide():
#     while True:
#         try:
#             n = input('Please sign your name here: ')
#             e = int(input('Please enter your english score here: '))
#             m = int(input('Please enter your math score here: '))
#             檢查成績_hide(e)
#             檢查成績_hide(m)
#
#         # 檢查整數輸入錯誤
#         except ValueError:
#             print("輸入錯誤，請輸入整數成績")
#         # 檢查其他錯誤
#         except Exception as err:
#             print(f'發生其他錯誤: {err} !!!')

def 輸入資料():
    while True:
        try:
            n = input('Please sign your name here: ')
            e = int(input('Please enter your english score here: '))
            m = int(input('Please enter your math score here: '))
            CheckPoint = [e, m]
            for i in CheckPoint:
                if 0 <= i <= 100 :
                    # 打包資料 > 寫成另一支 function
                    # Dlist = [n, e, m]
                    # return Dlist
                    return n, e, m
                else:
                    print("請輸入介於 0 ~ 100 的分數!")
                    break
        # 檢查整數輸入錯誤
        except ValueError:
            print("輸入錯誤，請輸入整數成績")
        # 檢查其他錯誤
        except Exception as err:
            print(f'發生其他錯誤: {err} !!!')

def 打包資料(n, e, m):
    DataPackage = [n, e, m]
    return DataPackage

def 輸入檔案名稱():
    FileName = input("請輸入要建立的檔案名稱: ")
    return FileName
def 儲存(FileName):
    print(f'--- 儲存資料: {FileName} ---')
    f = open(FileName, "w", encoding = 'UTF-8')
    s = f'{p[0]} {p[1]} {p[2]}'
    f.write(s)
    f.close()

def 讀取(FileName):
    print(f'--- 讀取資料: {FileName} ---')
    f = open(FileName, "r", encoding = 'UTF-8')
    for data in f :
        print(data)
    f.close()

# 主程式
# x = 輸入資料()
# print("x: ", x[0], x[1], x[2])

# x = 選擇選項()
# print("選項選擇為: ", x)

n, e, m = 輸入資料()
# print(n, e, m)
p = 打包資料(n, e, m)
FName = 輸入檔案名稱()
儲存(FName)
讀取(FName)

# 選擇選項()