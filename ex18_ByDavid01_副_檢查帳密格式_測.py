from ex18_ByDavid01_副_檢查帳密格式 import 檢查_密碼是否有數字
from ex18_ByDavid01_副_檢查帳密格式 import 檢查_密碼大寫英文字
from ex18_ByDavid01_副_檢查帳密格式 import 檢查_密碼大寫英文字_萬國碼, 檢查_密碼小寫英文字_萬國碼
from ex18_ByDavid01_副_檢查帳密格式 import 檢查_密碼任何英文字_萬國碼
from ex18_ByDavid01_副_檢查帳密格式 import 檢查帳號密碼格式
# import 亮起來的是 目前使用中的
# 可以分為多行 import 來增加可讀性

# x = 檢查_密碼是否有數字('1AB')
# print('1AB 檢查結果', x)
# x = 檢查_密碼是否有數字('AB1')
# print('AB1 檢查結果', x)
# x = 檢查_密碼是否有數字('ABC')
# print('ABC 檢查結果', x)

# 密 = 'Abc'
# x = 檢查_密碼大寫英文字(密)
# print(f'{密} 大寫字母 檢查結果 {x}')
# 密 = 'abC'
# x = 檢查_密碼大寫英文字(密)
# print(f'{密} 大寫字母 檢查結果 {x}')
# 密 = 'abc'
# x = 檢查_密碼大寫英文字(密)
# print(f'{密} 大寫字母 檢查結果 {x}')
# 密 = '111'
# x = 檢查_密碼大寫英文字(密)
# print(f'{密} 大寫字母 檢查結果 {x}')


# 密 = 'Abc'
# x = 檢查_密碼大寫英文字_萬國碼(密)
# print(f'{密} 大寫字母 檢查結果 {x}')
# 密 = 'abZ'
# x = 檢查_密碼大寫英文字_萬國碼(密)
# print(f'{密} 大寫字母 檢查結果 {x}')
# 密 = 'abz'
# x = 檢查_密碼大寫英文字_萬國碼(密)
# print(f'{密} 大寫字母 檢查結果 {x}')
# 密 = '111'
# x = 檢查_密碼大寫英文字_萬國碼(密)
# print(f'{密} 大寫字母 檢查結果 {x}')
#
#
# 密 = '張三45Z4'
# x = 檢查_密碼任何英文字_萬國碼(密)
# print(f'{密} 任一字母 檢查結果 {x}')

帳 = input("請輸入帳號: ")
密 = input("請輸入密碼: ")
if 檢查帳號密碼格式(帳, 密):
    print("帳號 密碼 格式符合")
else:
    print("帳號 密碼 格式不符合")