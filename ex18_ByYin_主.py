# 殷志忠老師(TeacherYin.com)
from ex18_ByYin_副_輸入帳密 import 輸入帳密
from ex18_ByYin_副_檢查帳密格式 import 檢查_帳, 檢查_密

a,b = 輸入帳密()
print('收到結果', a, b)
c = 檢查_帳(a)  # a 傳送到函數的區域變數 帳
print('收到 帳 長度 檢查結果', c)
d = 檢查_密(b)
print('收到 密 長度 檢查結果', d)