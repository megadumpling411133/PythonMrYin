# 殷志忠老師(TeacherYin.com)

# 輸入資料
n = input('輸入 name: ')
e = int(input('輸入 eng: '))
m = int(input('輸入 math: '))

# 打包資料 裝箱 list
a = [n, e, m]

# 檔案儲存
f = open('st3.txt', 'w')
s = f'{a[0]} {a[1]} {a[2]}'
f.write(s)
f.close()

print('--- 檔案讀取 ---')
f = open('st3.txt', 'r')
for s in f:
    print(s)
f.close()