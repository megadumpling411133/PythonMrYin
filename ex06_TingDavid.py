# 殷志忠老師(TeacherYin.com)
帳 = 'A001'
密 = '12345'
print(帳, 密)

正帳 = 'A001'
正密 = '12345'

if 帳 == 正帳 and 密 == 正密:
    print('登入成功')
    英 = 90
    數 = 80
    print(英, 數)
    if 英 >= 60 and 數 >= 60:
        print('英文 且 數學 及格 錄取')
        cm = float(input('輸入身高cm: '))
        kg = float(input('輸入體重kg: '))
    else:
        print('不錄取')
else:
    print('登入失敗 帳 或 密 錯誤')