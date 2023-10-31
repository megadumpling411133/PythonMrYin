# 殷志忠老師(TeacherYin.com)

英 = 90
數 = 50
print(英, 數)

# 註解 快速鍵 Ctrl+/

# if 英 >= 60:
#     print('錄取')

# if 數 >= 90:
#     print('錄取')
# else:
#     print('不錄取')

# if 英 >= 60:
#     print('英文及格 錄取')
# if 數 >= 60:  # if 一定會執行 與前面 if 無關
#     print('數學及格 錄取')

# if 英 >= 60:
#     print('英文及格 錄取')
# elif 數 >= 60:  # 前一個 if 不成立 elif 才會執行
#     print('數學及格 錄取')

# if 英 >= 60 or 數 >= 60:
#     print('英文 或 數學 及格 錄取')

if 英 >= 60 and 數 >= 60:
    print('英文 且 數學 及格 錄取')
else:
    print('不錄取')
