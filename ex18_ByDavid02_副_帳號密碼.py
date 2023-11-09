def 輸入帳號密碼(Flag):
    if Flag == 1:
        帳號 = input("請輸入帳號: ")
        密碼 = input("請輸入密碼: ")
        Flag = 1
        return 帳號, 密碼, Flag
def 設定帳號密碼(Flag):
    if Flag == 0:
        正確帳號 = input("請設定帳號: ")
        正確密碼 = input("請設定密碼: ")
        Flag = 1
    return 正確帳號, 正確密碼, Flag

def 檢查_帳密格式(正確帳號, 正確密碼):
    if len(正確帳號) <= 3 or len(正確密碼) <= 3:
        檢查結果 = True
        print("帳號 或 密碼設定需大於 3 碼，請重新設定")
    else:
        檢查結果 = False
        print("帳號 密碼 格式正確!!")
    return 檢查結果

def 驗證帳號密碼(帳號, 密碼, 正確帳號, 正確密碼):
    if 帳號 == 正確帳號 and 密碼 == 正確密碼:
        登入結果 = "成功登入"
    else:
        登入結果 = "帳號或密碼輸入錯誤!"

    return print(登入結果)