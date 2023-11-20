# 殷志忠老師(TeacherYin.com)
# 檔案處理
# https://www.w3schools.com/python/python_file_handling.asp

def 測試_儲存覆蓋():
    print('開啟 st.txt')
    f = open('st.txt', 'w')  # 開啟文字檔 寫入覆蓋
    # f = open('C:/Users/USER/Desktop/st.txt', 'w')  # 開啟文字檔 寫入覆蓋

    s = 'Tom 100 99'
    f.write(s)    # 寫入必須是字串
    print(f'寫入 {s}')
    f.write('\n')  # 寫入 換行
    print('寫入 換行')

    s = 'Amy 80 85'
    f.write(s)  # 寫入必須是字串
    print(f'寫入 {s}')
    f.write('\n')  # 寫入 換行
    print('寫入 換行')

    f.close()
    print('關閉 st.txt')


def 寫入字串換行(f,s):
    f.write(s)  # 寫入必須是字串
    print(f'寫入 {s}')
    f.write('\n')  # 寫入 換行
    print('寫入 換行')

def 測試_儲存覆蓋2():
    print('開啟 st.txt')
    f = open('st.txt', 'w')  # 開啟文字檔 寫入覆蓋
    # f = open('C:/Users/USER/Desktop/st.txt', 'w')  # 開啟文字檔 寫入覆蓋
    s = 'Tom 100 99'
    # f.write(s)  # 寫入必須是字串
    # print(f'寫入 {s}')
    # f.write('\n')  # 寫入 換行
    # print('寫入 換行')
    寫入字串換行(f,s)

    s = 'Amy 80 85'
    # f.write(s)  # 寫入必須是字串
    # print(f'寫入 {s}')
    # f.write('\n')  # 寫入 換行
    # print('寫入 換行')
    寫入字串換行(f, s)

    f.close()
    print('關閉 st.txt')

def 測試_儲存追加():
    filename = 'st2.txt'
    print(f'開啟 附加 {filename}')
    f = open(filename, 'a')  # 開啟文字檔 寫入附加
    n = 'Tom'
    e = 100
    m = 99
    s = f'{n}\n'
    f.write(s)
    s = f'{e}\n'
    f.write(s)
    s = f'{m}\n'
    f.write(s)
    f.close()
    print(f'關閉 {filename}')

def 讀取三行():
    filename = 'st2.txt'
    print(f'開啟 讀取三行 {filename}')
    f = open(filename, 'r')  # 開啟文字檔 讀取
    s = f.readline()
    # 注意 replace() 將取代結果以新字串返回 原本s字串無法修改
    s2 = s.replace('\n', '')  # replace(尋找字串,替換字串)
    print(s2)
    s = f.readline()
    s2 = s.replace('\n', '')  # replace(尋找字串,替換字串)
    print(s2)
    s = f.readline()
    s2 = s.replace('\n', '')  # replace(尋找字串,替換字串)
    print(s2)
    f.close()
    print(f'關閉 {filename}')

# open()
# https://docs.python.org/zh-tw/3.9/library/functions.html#open
def 讀取for():
    filename = 'st2.txt'
    print(f'開啟 for 讀取每一行 {filename}')
    f = open(filename, 'r', encoding = 'UTF-8')  # 開啟文字檔 讀取
    for s in f:
        # 注意 replace() 將取代結果以新字串返回 原本s字串無法修改
        s2 = s.replace('\n', '')  # replace(尋找字串,替換字串)
        print(s2)
    f.close()
    print(f'關閉 {filename}')

# 測試_儲存覆蓋()
# 測試_儲存覆蓋2()
# 測試_儲存追加()
# 讀取三行()
讀取for()