At_Correct = "A001"
PW_Correct = "12345"
ticky = ""
for i in range(3): # 0 ~ 2 , 3 不包含
    print(i)
    Account = input("Please enter your Account: ")
    PassWord = input("Please enter your PassWord: ")

    if Account != At_Correct or PW_Correct != "12345":
        # CheckPoint = "Block" # 已經進入錯誤區條件 不需要再吃一個檢查點
        print("帳號 或 密碼錯誤")
        # 檢查第幾次錯誤
        if i == 2:
            print("錯誤達3次，不可登入")
            break
    else:
        print("登入成功")
        break

print('-------------')

# 加入檢查點題示錯誤 3 次
# At_Correct = "A001"
# PW_Correct = "12345"
# for i in range(3): # 0 ~ 2 , 3 不包含
#     print(i)
#     Account = input("Please enter your Account: ")
#     PassWord = input("Please enter your PassWord: ")
#
#     if Account != At_Correct or PW_Correct != "12345":
#         CheckPoint = "Block"
#         print("帳號 或 密碼錯誤")
#         print(CheckPoint)
#         if i == 2 and CheckPoint == "Block":
#             print("錯誤達3次，不可登入")
#     else:
#         CheckPoint = "Pass"
#         print("登入成功")
#         print(CheckPoint)
#         break
# print('-------------')