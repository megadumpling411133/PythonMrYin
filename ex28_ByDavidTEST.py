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
                        action = "輸入檔名"
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
                    print("請輸入選項範圍: 動作(0 ~ 4) 或是 結束(9) \n請重新輸入")
        # 檢查整數輸入錯誤
        except ValueError:
            print("輸入錯誤，請輸入整數數字")
        # 檢查其他錯誤
        except Exception as err:
            print(f'發生其他錯誤: {err} !!!')

# def 檢查分數(CheckPoint):
#     Result = False
#     while True:
#         for i in CheckPoint[0]:
#             if 0 <= i <= 100:
#                 # 打包資料 > 寫成另一支 function
#                 # Dlist = [n, e, m]
#                 # return Dlist
#                 print("aaa")
#                 Result = True
#                 # return Result
#                 for i in CheckPoint[1]:
#                     if 0 <= i <= 100:
#                         print("asdad")
#                         Result = True
#                 return Result
#             else:
#                 print("bbb")
#                 Result = False
#                 print("請輸入介於 0 ~ 100 的分數!")
#                 # break
#                 # return Result

# def 輸入資料():
#     while True:
#         try:
#             n = input('Please sign your name here: ')
#             e = int(input('Please enter your english score here: '))
#             # CheckPoint = [e, m]
#             檢查分數(CheckPoint)
#             m = int(input('Please enter your math score here: '))
#             CheckPoint = [e, m]
#             檢查分數(CheckPoint)
#             return n, e, m
#         # 檢查整數輸入錯誤
#         except ValueError:
#             print("輸入錯誤，請輸入整數成績")
#         # 檢查其他錯誤
#         except Exception as err:
#             print(f'發生其他錯誤: {err} !!!')

# def 檢查分數(score):
#     if 0 <= score <= 100:
#         return True
#     else:
#         print("輸入錯誤，請輸入介於 0 ~ 100 的分數")
#         return False

# def 檢查分數(score):
#     if 0 <= score <= 100:
#         return True
#     else:
#         print("輸入錯誤，請輸入介於 0 ~ 100 的分數")
#         return False

def 檢查分數(score):
    if 0 <= score <= 100:
        return True
    else:
        print("輸入錯誤，請輸入介於 0 ~ 100 的分數")
        return False

# def 檢查分數(score):
#     if 0 <= score <= 100:
#         return True
#     else:
#         print("輸入錯誤，請輸入介於 0 ~ 100 的分數")
#         return False

def 輸入資料():
    n = None  # 初始時將名字設為 None

    while True:
        try:
            e = int(input('Please enter your english score here: ')

            if not 檢查分數(e):
                continue  # 重新輸入英文分數

            m = int(input('Please enter your math score here: '))
            if not 檢查分數(m):
                continue  # 重新輸入數學分數

            return n, e, m
        except ValueError:
            print("輸入錯誤，請輸入整數成績")
        except Exception as err:
            print(f'發生其他錯誤: {err} !!!')

# def 輸入資料():
#     while True:
#         try:
#             n = input('Please sign your name here: ')
#             e = int(input('Please enter your english score here: '))
#             m = int(input('Please enter your math score here: '))
#             CheckPoint = [e, m]
#             if 檢查分數(CheckPoint):
#                 return n, e, m
#         except ValueError:
#             print("輸入錯誤，請輸入整數成績")
#         except Exception as err:
#             print(f'發生其他錯誤: {err} !!!')

def 打包資料():
    if n or e or m is None:
        print("尚未輸入資料，請先輸入資料")
        return
    try:
        DataPackage = [n, e, m]
        return DataPackage
    except ValueError:
        print("目前尚未輸入資料，請輸入資料")
    # except Exception as err:
    #     print(f'發生其他錯誤: {err} !!!')

def 輸入檔案名稱():
    try:
        FileName = input("請輸入要建立的檔案名稱: ")
        print(f"預計建立的檔案名稱: {FileName}")
        return FileName
    except Exception as err:
        print(f'發生其他錯誤: {err} !!!')

def 儲存_覆蓋(FileName):
    print(f'--- 儲存資料: {FileName} ---')
    if FileName is None:
        FileName = 輸入檔案名稱()
    if Package is None:
        print("檔案儲存_覆蓋失敗，尚未打包資料")
        return

    f = open(FileName, "w", encoding = 'UTF-8')
    s = f'{Package[0]} {Package[1]} {Package[2]}'
    f.write(s)
    f.close()
    print("儲存_覆蓋成功")

def 儲存_附加(FileName):
    print(f'--- 儲存資料: {FileName} ---')
    if Package is None:
        print("檔案儲存_附加失敗，尚未打包資料")
        return
    f = open(FileName, "w", encoding = 'UTF-8')
    s = f'{Package[0]} {Package[1]} {Package[2]}'
    f.write(s)
    f.close()
    print("儲存_附加成功")

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

# n, e, m = 輸入資料()
# # print(n, e, m)
# p = 打包資料(n, e, m)
# FName = 輸入檔案名稱()
# 儲存(FName)
# 讀取(FName)

# 選擇選項()
n, e, m = None, None, None
Package = [n, e, m]      # 預設未打包
FileName = None
def 執行():
    while True:
        op = 選擇選項()
        global FileName
        if FileName is None:
            print("尚未輸入檔案名稱，請先輸入檔案名稱")
            FileName = 輸入檔案名稱()
            op = 選擇選項()
            return
        else:
        # try:
            if op == 1:
                # n, e, m = 輸入資料()
                Package = 輸入資料()
            elif op == 2:
                Package = 打包資料()
            elif op == 3:
                儲存_覆蓋()
            elif op == 4:
                讀取()
            elif op == 9:
                    break
        # except Exception as err:
        #     print(f'發生其他錯誤: {err} !!!')
# 執行()
輸入資料()
print('--- 結束 ---')