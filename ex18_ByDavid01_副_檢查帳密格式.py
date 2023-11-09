def 檢查_帳密格式(正確帳號, 正確密碼):
    if len(正確帳號) <= 3 or len(正確密碼) <= 3:
        檢查結果 = True
        print("帳號 或 密碼 設定需大於 3 碼，請重新設定")
    else:
        檢查結果 = False
        # print("帳號 密碼 格式正確!!")
    return 檢查結果

def 檢查_帳長度(正確帳號):
    if len(正確帳號) <= 3:
        檢查結果 = False
        print("帳號 設定需大於 3 碼，請重新設定")
    else:
        檢查結果 = True
        # print("帳號 大於 3 碼 格式正確!!")
    return 檢查結果

def 檢查_密長度(正確密碼):
    if len(正確密碼) <= 4:
        檢查結果 = False
        print("密碼 設定需大於 4 碼，請重新設定")
    else:
        檢查結果 = True
        # print("密碼 大於 4 碼 格式正確!!")
    return 檢查結果

def 檢查_密碼是否有數字(密):
    #print("====================")
    #print(密)
    # in 後可直接給可迭代 變數 for loop 會逐次進入
    for i in 密:
        #print(i)
        #if i == "0123456789": # 這段會出錯是因為 檢查了 i 是否等於 "0123456789"
        if i in "0123456789":
            #print(i)
            # print("密碼含有數字")
            return True # 其中一碼有數字即可
    print("密碼 不含數字，請重新設定")

    return False

def 檢查_密碼大寫英文字(密):
    for i in 密:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return True
    return False

def 檢查_密碼大寫英文字_萬國碼(密): # 萬國碼 UTF-8 方式檢查
    for i in 密:
        if 65 <= ord(i) <= 90:
            # print("密碼 包含大寫字母")
            return True
    print("密碼 不包含大寫字母，請重新設定")
    return False

def 檢查_密碼小寫英文字_萬國碼(密): # 萬國碼 UTF-8 方式檢查
    for i in 密:
        if 97 <= ord(i) <= 122:
            # print("密碼 包含大寫字母")
            return True
    print("密碼 不包含大寫字母，請重新設定")
    return False

def 檢查_密碼任何英文字_萬國碼(密): # 萬國碼 UTF-8 方式檢查
    for i in 密:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            # print("密碼 包含字母")
            return True
    print("密碼 不包含字母，請重新設定")
    return False

def 檢查帳號密碼格式(正確帳號, 正確密碼):

    #CheckPoint
    P1 = 檢查_帳長度(正確帳號)

    P2 = 檢查_密長度(正確密碼)
    P3 = 檢查_密碼是否有數字(正確密碼)
    P4 = 檢查_密碼任何英文字_萬國碼(正確密碼)

    # if P1 == True and P2 == True and P3 == True and P4 == True:
    # if P1 and P2 and P3 and P4:
    #     print("密碼檢查通過")
    return P1 and P2 and P3 and P4