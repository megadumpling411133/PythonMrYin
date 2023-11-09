def 檢查_密碼是否有數字(密):
    print("====================")
    print(密)
    # in 後可直接給可迭代 變數 for loop 會逐次進入
    for i in 密:
        print(i)
        #if i == "0123456789": # 這段會出錯是因為 檢查了 i 是否等於 "0123456789"
        if i in "0123456789":
            print(i)
            print("密碼含有數字")
            return True # 其中一碼有數字即可
    print("密碼不含數字")

    return False