# 殷志忠老師(TeacherYin.com)
from ex18_副_檢查帳密格式 import 檢查_密_出現數字, 檢查_密_出現大寫英文字母, 檢查_密_出現大寫英文字母_萬國碼

# x = 檢查_密_出現數字('1AB')
# print('1AB 檢查結果', x)
# 檢查_密_出現數字('AB1')
# print('AB1 檢查結果', x)
# 檢查_密_出現數字('ABC')
# print('ABC 檢查結果', x)

# 密 = 'Abc'
# x = 檢查_密_出現大寫英文字母(密)
# print(f'{密} 大寫字母 檢查結果 {x}')
# 密 = 'abC'
# x = 檢查_密_出現大寫英文字母(密)
# print(f'{密} 大寫字母 檢查結果 {x}')
# 密 = 'abc'
# x = 檢查_密_出現大寫英文字母(密)
# print(f'{密} 大寫字母 檢查結果 {x}')
# 密 = '111'
# x = 檢查_密_出現大寫英文字母(密)
# print(f'{密} 大寫字母 檢查結果 {x}')


密 = 'Abc'
x = 檢查_密_出現大寫英文字母_萬國碼(密)
print(f'{密} 大寫字母 檢查結果 {x}')
密 = 'abZ'
x = 檢查_密_出現大寫英文字母_萬國碼(密)
print(f'{密} 大寫字母 檢查結果 {x}')
密 = 'abz'
x = 檢查_密_出現大寫英文字母_萬國碼(密)
print(f'{密} 大寫字母 檢查結果 {x}')
密 = '111'
x = 檢查_密_出現大寫英文字母_萬國碼(密)
print(f'{密} 大寫字母 檢查結果 {x}')