def 輸入英文成績():
    while True:
        eng = int(input("請輸入 英文 成績 (輸入分數需介於 0 ~ 100 之間): "))
        # if 0 > eng > 100 :
        if 0 > eng or eng > 100:
            print("注意, 輸入之 英文 成績需要介於 0 ~ 100 之間")
        else:
            # print("輸入英文分數為: " + str(eng))
            # break # break 只會結束迴圈 效力小於 return
            return eng  # return 最大 直接終止程式 返回結果


def 輸入數學成績():
    while True:
        mat = int(input("請輸入 數學 成績 (輸入分數需介於 0 ~ 100 之間): "))
        if 0 > mat or mat > 100:
            print("注意, 輸入之 數學 成績需要介於 0 ~ 100 之間")
        else:
            # print("輸入數學分數為: " + str(mat))
            return mat


def 顯示輸入之成績(eng, mat):
    eng = str(eng)
    mat = str(mat)
    Br = "\n"
    print("輸入之英文成績: " + eng + Br + "輸入之數學成績: " + mat)


def 執行():
    eng = 輸入英文成績()
    mat = 輸入數學成績()
    顯示輸入之成績(eng, mat)

# 主程式
執行()
