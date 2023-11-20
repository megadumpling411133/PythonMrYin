# 檔案處理
def save_write_v1(p):   # 儲存覆蓋 版本1 v1
    print(f'開啟檔案路徑 {p}')
    f = open(p, 'w')

    str = 'Abbie 100 100'
    f.write(str)
    f.write('\n')

    str = 'Bob 100 100'
    f.write(str)
    f.write('\n')

    f.close()
    print(f"關閉: {p}")

def write_break(f, s):  # 寫入換行
    f.write(s)
    print(f'寫入 {s}')
    f.write('\n')
    print('寫入 換行')

def save_write_v2(p):   # 儲存覆蓋 版本2 v2
    print(f'開啟檔案路徑 {p}')
    f = open(p, 'w')
    str = 'Abbie 100 100'
    write_break(f, str)

    str = 'Bob 100 100'
    write_break(f, str)

    f.close()
    print(f"關閉: {p}")

def save_append_v2(path, name, eng, math):      # 儲存追加 版本1 v1
    FileName = path
    print(f'開啟 附加')
    f = open(FileName, 'a') # a 表示 append

    # str = f'{name}\n'
    # f.write(str)
    # str = f'{eng}\n'
    # f.write(str)
    # str = f'{math}\n'
    str = f'{name} {eng} {math}\n'
    f.write(str)

    # f.write(name, eng, math) # 不行這樣用
    f.close()
    print(f'關閉 {FileName}')
def save_append_v1(path, name, eng, math):      # 儲存追加 版本1 v1
    # FileName = 'str.txt'
    FileName = path
    print(f'開啟 附加')
    f = open(FileName, 'a') # a 表示 append
    # name = 'Dennis'
    # eng = 100
    # math = 99

    str = f'{name}\n'
    f.write(str)
    str = f'{eng}\n'
    f.write(str)
    str = f'{math}\n'
    f.write(str)

    f.close()
    print(f'關閉 {FileName}')

def readLineTo3():
    FileName = 'str.txt'

    # 讀取 r 可省略 為預設開啟檔案模式
    # f = open(FileName, 'r')
    f = open(FileName)
    # 讀取一行 readline()
    s = f.readline()
    # 注意: replace 會將處理(取代)結果返回,不會取代原值
    # 所以要存入另一變數來保留處理結果
    s2 = s.replace('\n', "")
    print(s2)
    # 也可以這樣 一氣呵成的處理 再存入原變數
    # s = f.readline().replace('\n', "")
    s = f.readline()
    s2 = s.replace('\n', "")
    print(s2)
    s = f.readline()
    s2 = s.replace('\n', "")
    print(s2)
    f.close()
    print(f'關閉 {FileName}')

def 逐行讀取for(p):
    # FileName = 'str2.txt'
    FileName = p
    print(f'開啟 {FileName} 迴圈讀取檔案每一行')
    # 開啟檔案 可以設定 檔案來源 編碼方式   來避免編碼錯誤造成開啟錯誤
    f = open(FileName, encoding='UTF-8')      # 預設開啟模式 r 可省略
    for str in f:
        # 注意: replace 會將處理(取代)結果返回,不會取代原值
        # str2 = str.replace("\n", '')
        # print(str2)
        str = str.replace("\n", '')
        print(str)
    f.close()
    print(f'關閉 {FileName}')


# https://docs.python.org/zh-tw/3.9/library/functions.html#open
# 開啟檔案 可以設定 檔案來源 編碼方式
# f = open(FileName, 'r', encodeing = '檔案來源編碼方式 e.g UTF-8')

# save_write_v1('str1.txt')
# save_write_v2('str2.txt')
save_append_v2('str2.txt', 'Inna', '77', '66')
逐行讀取for("str2.txt")


