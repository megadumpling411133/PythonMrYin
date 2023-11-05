# print()  # 沒有傳遞資料 也沒有返回資料
print("AA")
資料 = '歡迎光臨'
print("Bb")
結果 = print(資料)  # None 沒東西 空值 因為 print() 沒有 return 值
print("Cc")
print(結果)
print("Dd")

資料 = '請輸入密碼'
print("EE")
結果 = input(資料) # 請輸入密碼 因為 input() 有 return 值
print("FF")
print(結果)
