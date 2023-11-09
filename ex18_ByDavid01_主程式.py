from ex18_ByDavid01_副_設定帳號密碼 import 設定帳號密碼
from ex18_ByDavid01_副_檢查帳密格式 import 檢查_帳密格式, 檢查_密碼是否有數字
#Flag = 0
#設定帳號密碼(Flag)
a,b,c = 設定帳號密碼(0)
print('收到結果', a, b)
d = 檢查_帳密格式(a,b)  # a 傳送到函數的區域變數 帳
print('收到 帳 密 長度 檢查結果', d)
e = 檢查_密碼是否有數字(b)
print('收到 密 是否有數字 檢查結果', e)