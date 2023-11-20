# 殷志忠老師(TeacherYin.com)
import csv
# with open 會自動關閉檔案
with open('ex32.csv', newline='', encoding='utf-8') as f:
    # f 代表檔案
    # r 代表閱讀器
    r = csv.reader(f, delimiter=',')  # delimiter 資料分隔符號 預設為 ,
    欄 = next(r)  # next() 讀取一行
    print('欄', 欄)  # 串列
    for 筆 in r:  #
        print('讀一筆資料', 筆)  # 串列
        n,e,m = 筆
        e,m = int(e), int(m)
        print('拆解', n,e,m)
print('--- 檔案自動關閉 ---')