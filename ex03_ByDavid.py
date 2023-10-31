# 英 = 80
# 數 = 80

英 = input("請輸入英文成績: ")
數 = input("請輸入數學成績: ")
Break = "\n"
print("英文分數: " + str(英) + Break + "數學分數: " + str(數) + Break)
英 = int(英)
數 = int(數)
# 註解 快速鍵 Ctrl+/

# if 獨立條件判斷 的開始
# 與 其他 if 無關

# 當 if 判斷 false 之後 可以接上 else 或者 elif

# else 當 if 判斷 False 無條件執行 else
# elif 當 前一個 if 或 前一的 elif 判斷 False 執行本條件判斷

# else 關鍵字 表示 當前一判斷式 False 之後進入

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

# if 英 >= 60 and 數 >= 60:
#     print('英文 且 數學 及格 錄取')
# else:
#     print('不錄取')


# if 英 >= 60 and 數 >= 60:
#     print('英文 且 數學 及格 錄取')
# else:
#     if 英 < 60 and 數 < 60:
#         print('英文 數學 都不及格 不錄取')
#     elif 英 < 60 :
#         print('英文 不及格 不錄取')
#     elif 數 < 60:
#         print('數學 不及格 不錄取')


# if 英 == 100:
#     print("英文滿分 無條件錄取")
# elif 英 >= 60 and 數 >= 60:
#     print('英文 且 數學 及格 錄取')
# else:
#     if 英 < 60 and 數 < 60:
#         print('英文 數學 都不及格 不錄取')
#     elif 英 < 60 :
#         print('英文 不及格 不錄取')
#     elif 數 < 60:
#         print('數學 不及格 不錄取')


if 英 == 0 or 數 == 0:
    print("英文 或 數學 0 分 不錄取")
elif 英 == 100:
    print("英文滿分 無條件錄取")
elif 英 >= 60 and 數 >= 60:
    print('英文 且 數學 及格 錄取')
else:
    if 英 < 60 and 數 < 60:
        print('英文 數學 都不及格 不錄取')
    elif 英 < 60 :
        print('英文 不及格 不錄取')
    elif 數 < 60:
        print('數學 不及格 不錄取')