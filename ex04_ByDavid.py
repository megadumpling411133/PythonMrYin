帳 = input('請輸入帳號: ')
密 = input('請輸入密碼: ')
Br = "\n"
print("帳號: " + 帳 + Br + "密碼: " + 密)

正確帳號 = 'A001'
正確密碼 = '1234'

# 帳號驗證
if 帳 == 正確帳號 and 密 == 正確密碼:
    print('登入成功')
    # 輸入成績
    英 = input("請輸入英文分數: ")
    數 = input("請輸入數學分數: ")
    print("英文成績: " + 英 + Br + "數學成績: " + 數)
    英 = int(英)
    數 = int(數)
    # 判斷錄取與否
    if 英 == 0 or 數 == 0:
        print("英文 或 數學 0 分 不錄取")
    elif 英 == 100:
        print("英文滿分 無條件錄取")
    elif 英 >= 60 and 數 >= 60:
        print('英文 且 數學 及格 錄取')
    else:
        if 英 < 60 and 數 < 60:
            print('英文 數學 都不及格 不錄取')
        elif 英 < 60:
            print('英文 不及格 不錄取')
        elif 數 < 60:
            print('數學 不及格 不錄取')
else:
    print('登入失敗 帳號 或 密碼 錯誤')


# UserName = input('')