# 殷志忠老師(TeacherYin.com)

s = '''
1. 輸入資料
2. 打包資料
3. 儲存資料
4. 讀取資料
請選擇: 
'''
op = int(input(s))
if op < 1 or op > 4:
    print('輸入錯誤，沒有這個選項')