Account = input('請輸入帳號: ')
PassWard = input('請輸入密碼: ')

Ac_Correct = 'A001'
Pa_Correct = '12345'

if Account == Ac_Correct and PassWard == Pa_Correct:
    print('登入成功!')
else:
    print('登入失敗 帳號 或 密碼 錯誤')