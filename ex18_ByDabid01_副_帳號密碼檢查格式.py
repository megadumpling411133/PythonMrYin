def 檢查_帳密格式(正確帳號, 正確密碼):
    if len(正確帳號) <= 3 or len(正確密碼) <= 3:
        檢查結果 = True
        print("帳號 或 密碼設定需大於 3 碼，請重新設定")
    else:
        檢查結果 = False
        print("帳號 密碼 格式正確!!")
    return 檢查結果