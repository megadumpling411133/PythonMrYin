# 殷志忠老師(TeacherYin.com)

# 別人提供資料
# 帳 = 'aa'
def 檢查_帳(帳):  # 區域變數 帳
    # print(帳)
    if len(帳) >= 3:
        print('帳號長度 符合 >= 3')
        return True
    else:
        print('帳號長度 不符合 >= 3')
        return False

def 檢查_密(密):
    # print('檢查_密 功能尚未完成')
    pass

def 檢查_密_出現大寫英文字母(密):
    for i in 密:  # 逐項讀取每一個字
        if i in 'ABCDE': # 若 i 有出現在字串中:
            return True
    return False

def 檢查_密_出現大寫英文字母_萬國碼(密):
    for i in 密:  # 逐項讀取每一個字
        if 65 <= ord(i) <= 90:
            return True
    return False