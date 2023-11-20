# 殷志忠老師(TeacherYin.com)
from ex19_ByYin_副 import 輸入帳密, 檢查_帳, 檢查_密

帳,密 = 輸入帳密()

print('----------- 帳號')
if 檢查_帳(帳):
    print('OK')
else:
    print('不OK')


print('----------- 密碼')
if 檢查_密(密):
    print('OK')
else:
    print('不OK')