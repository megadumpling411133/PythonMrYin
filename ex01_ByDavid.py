# 變數賦值 四則運算

# 重新命名檔案 重構(ReFactor) > 重新命名(ReName) > ShortCut Shift F6 )

# 功能 也叫 函數 function (服務生)

# print() 顯示資料

# 資料類型 Data Types > 搜尋關鍵字(W3C標準): 語言名稱 + Data Types > e.g Python Data Types W3C
#   整數 int
#   浮點數 float 電腦使用 2 進制，不一定能算出真實數字 > 因此浮點數可能為近似值 例如 0.1 的近似值(所見 0.1 不為所得 0.1 的近似值)
#   文字 str  用單雙引號包含 quotes('文字內容 AAA...') or double quotes("文字內容 BBB...")

# 運算
#   + - * / %
#   原值運算(我自己亂取的) += -= *=

print(100)
print(0.1)
print('Tom')

x = 5
x += 3
print(x)
x -= 3
print(5)
x *= 2
print(x)

名 = 'Tom'
英 = 100
數 = 99
總 = 英 + 數
平 = 總 / 2
print(名, 英, 數, 總, 平)

# 加入描述 使用 + 號 來串接字串 > 將 非字串轉為字串
print("姓名: " + str(名),"英文分數: " +  str(英),"數學分數: " +  str(數),"總分: " +  str(總),"平均: " +  str(平))



