from ex18_ByDavid02_副_帳號密碼 import 輸入帳號密碼,設定帳號密碼,驗證帳號密碼,檢查_帳密格式
Flag = 0




if Flag == 0:   # 第一次使用 設定帳密
    正確帳號, 正確密碼, Flag = 設定帳號密碼(Flag)
    檢查_帳密格式(正確帳號, 正確密碼)
if Flag == 1: # 第一次之後使用 檢查帳密
    帳號, 密碼 = 輸入帳號密碼(Flag)
    驗證帳號密碼(帳號, 密碼, 正確帳號, 正確密碼)
    print(正帳, 正密)



