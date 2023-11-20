# 殷志忠老師(TeacherYin.com)

def 輸入帳密():
    帳 = input('輸入帳號:')
    密 = input('輸入密碼:')
    return 帳,密

def 出現數字(字串):
    for i in 字串:  # 逐項讀取每一個字
        # print('讀到', i)
        if i in '0123456789': # 若 i 有出現在字串中:
            return True
    print('錯誤：沒有數字')
    return False

def 出現大寫(字串):
    for i in 字串:  # 逐項讀取每一個字
        if 65 <= ord(i) <= 90:
            return True
    print('錯誤：沒有大寫')
    return False

def 長度大於等於3(字串):
    # return len(字串) >= 3
    if len(字串) >= 3:
        return True
    print('錯誤：長度不足3個字')
    return False

def 檢查_帳(帳):  # 區域變數 帳
    x1 = 長度大於等於3(帳)
    x2 = 出現大寫(帳)
    return x1 and x2

def 檢查_密(密):
    x1 = 長度大於等於3(密)
    x2 = 出現大寫(密)
    x3 = 出現數字(密)
    return x1 and x2 and x3