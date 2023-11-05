# function 定義功能 越單一 越簡單 未來越好除錯

def 輸入帳密():
    帳 = input('請輸入帳號: ')
    密 = input('請輸入密碼: ')
    return 帳, 密

def 驗證帳密(帳, 密):
    正帳 = "A001"
    正密 = "12345"

    return 帳 == 正帳 and 密 == 正密 # return 判斷結果 boolean value 正確 True 錯誤 False

def 限制錯誤次數(帳, 密):
    for i in range(3):
        # 縮排 TAB
        p = input('請輸入密碼:')
        if p == '123':
            print('登入成功')
            break  # 立刻結束迴圈
        else:
            print('密碼錯誤')

def 登入成功流程():
    print("登入成功!")
    # 成功時要做的事情()
def 登入失敗流程():
    print("登入失敗, 帳號 或 密碼 錯誤!")
    # 失敗時要做的事情()

def 失敗時檢查上限():
    print("12313")

def 執行():
    帳, 密 = 輸入帳密()
    if 驗證帳密(帳, 密):
        登入成功流程()
    else:
        登入失敗流程()
# 主流程
執行()

# 帳, 密 = 輸入帳密()
# if 驗證帳密(帳, 密):
#     登入成功流程()
# else:
#     登入失敗流程()
#
# def 嘗試次數():
#     At_Correct = "A001"
#     PW_Correct = "12345"
#     ticky = ""
#     for 嘗試次數 in range(3): # 0 ~ 2 , 3 不包含
#         print(嘗試次數)
#         Account = input("Please enter your Account: ")
#         PassWord = input("Please enter your PassWord: ")
#
#         if Account != At_Correct or PW_Correct != "12345":
#             # CheckPoint = "Block" # 已經進入錯誤區條件 不需要再吃一個檢查點
#             print("帳號 或 密碼錯誤")
#             # 檢查第幾次錯誤
#             if 嘗試次數 == 2:
#                 print("錯誤達3次，不可登入")
#                 break
#         else:
#             print("登入成功")
#             break
#
#     print('-------------')
