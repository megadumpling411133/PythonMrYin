# 錯誤(例外)處理

def T1():
    try:# 想執行但可能發生錯誤的程式
        # 這裡的程式碼會被接住錯誤
        # 若錯誤發生，會中止執行，並進入 except 區塊處理錯誤
        e = int(input('請輸入英文成績: '))
        # 上一行出錯，下面程式會被略過，跳到 except 錯誤處理
        # x = e / 0  # ZeroDivisionError: division by zero
        print('輸入完成')
    # except ValueError:
    #     # except 的程式碼，在錯誤發生之後會被執行
    #     # 可指定錯誤類型: ValueError 的處理方式
    #     print('錯誤: 請輸入整數數字格式')
    except Exception  as otherError:   # 不建議這樣忽略錯誤
        # 不指定會接住所有其他錯誤
        print(f'其他錯誤: {otherError} 發生了')
    print('END')

def genDate_EngScore():
    while True: # 無條件執行迴圈
        try:
            eng = int(input('please enter your english score: '))
            # 若執行失敗 會進入 except
            # 若執行成功 會進入下一行
            return eng
        except ValueError:
            print('輸入錯誤: 請輸入整數數字格式')

T1()
# genDate_EngScore()