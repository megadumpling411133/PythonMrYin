def 輸入帳密():
    帳 = input("請輸入帳號: ")
    密 = input("請輸入密碼: ")
    return 帳, 密

def 長度大於等於_hide(目標字串, 檢查數字): # 不論整數 浮點數都會進入檢查 Int 的 else
    if type(檢查數字) == "int":
        p1 = len(目標字串) >= 檢查數字
        Check_int = True
    else:
        print("函式_長度大於等於(目標字串, 檢查數字)使用錯誤 第二參數需要給予整數")
        # Check_int = False
        return
    # p1 = len(目標字串) >= 檢查數字

    if p1 and Check_int:
        pass # if 之內一定要有程式碼
        # print(f"檢查合格: 長度大於等於 {檢查數字}")
    else:
        print(f"檢查不合格: 長度小於 {檢查數字}")

    return p1

def 長度大於等於(目標字串, 檢查數字):
    p1 = len(目標字串) >= 檢查數字

    if p1 :
        pass # if 之內一定要有程式碼
        # print(f"檢查合格: 長度大於等於 {檢查數字}")
    else:
        print(f"檢查不合格: 長度小於 {檢查數字}")

    return p1

def 檢查數字(目標字串):
    for i in 目標字串:
        if i in "0123456789":
            # print(f"檢查合格: 包含數字")
            return True
    print(f"檢查不合格: 不包含數字")

    return False
def 檢查大寫(目標字串):
    for i in 目標字串:
        if 65 <= ord(i) <= 90:
            # print(f"檢查合格: 包含大寫字母")
            return True
    print(f"檢查不合格: 不包含大寫字母")
    return False

def 檢查小寫(目標字串):
    for i in 目標字串:
        if 97 <= ord(i) <= 122:
            # print(f"檢查合格: 包含小寫字母")
            return True
    print(f"檢查不合格: 不包含小寫字母")
    return False

def 檢查字母(目標字串):
    for i in 目標字串:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            # print(f"檢查合格: 包含字母")
            return True
    print(f"檢查不合格: 不包含字母")

    return False

def 檢查帳號(帳號):
    p1 = 長度大於等於(帳號, 4)
    p2 = 檢查字母(帳號)


    return p1 and p2

def 檢查密碼(密碼):
    p1 = 長度大於等於(密碼, 6)
    p3 = 檢查大寫(密碼)
    p2 = 檢查數字(密碼)

    return p1 and p2 and p3
