# 讀取 excel .csv 檔案
import csv
# with 開啟檔案 會幫忙自動關閉
with open('ex32.csv', newline = '', encoding = 'UTF-8') as f:
    # f 代表檔案
    # r 代表閱讀器
    r = csv.reader(f, delimiter = ',') # delimiter 資料分隔符號，預設值為 comma 逗號 ","
    欄 = next(r) # next() 讀取一行
    print(f'欄: {欄}')
    i = 1
    for 筆 in r:
        print(f'讀取第 {i} 筆資料: {筆}')
        n, e, m = 筆
        e, m = int(e), int(m)
        print(f'拆解: {n, e, m}')
        i += 1
print('====== with 自動關閉檔案 ======')