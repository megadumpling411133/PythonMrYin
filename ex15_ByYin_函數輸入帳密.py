# 殷志忠老師(TeacherYin.com)

def 輸入帳密():
    帳 = input('輸入帳號:')
    密 = input('輸入密碼:')
    return 帳, 密

def 驗證帳密():
    正帳 = 'A001'
    正密 = '12345'
    return 帳 == 正帳 and 密 == 正密  # 返回 True 或 False

def 登入成功流程():
    print('登入成功')

def 登入失敗流程():
    print('登入失敗 帳 或 密 錯誤')

# 主流程
帳, 密 = 輸入帳密()
# print(帳, 密)
# 結果 = 驗證帳密()  # 返回 True 或 False
# print(結果)
if 驗證帳密():
    登入成功流程()
else:
    登入失敗流程()