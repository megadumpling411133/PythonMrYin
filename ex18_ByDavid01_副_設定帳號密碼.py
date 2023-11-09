def 設定帳號密碼(Flag):
    if Flag == 0:
        正確帳號 = input("請設定帳號: ")
        正確密碼 = input("請設定密碼: ")
        Flag = 1
    return 正確帳號, 正確密碼, Flag