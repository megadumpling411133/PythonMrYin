option = '''可選動作選單: 
    1. 輸入資料
    2. 打包資料
    3. 儲存資料
    4. 讀取資料
'''
# op = int(input(option))
# if op < 1 or op > 4:
#     print('輸入錯誤，沒有這個選項')


# 測試中
try:
    while True:
        op = int(input(f"{option}請輸入選擇為編號:"))
        if 0 < op <= 4:
            if op == 1:
                action = "1. 輸入資料"
            elif op == 2:
                action = "2. 打包資料"
            elif op == 3:
                action = "3. 儲存資料"
            elif op == 4:
                action = "4. 讀取資料"
            print(f"目前選擇選項為: {action}")
            break
            # return op
        else:
            print("請輸入選項範圍: 1 ~ 4 \n請重新輸入")
except ValueError:
    print("輸入錯誤，請輸入整數數字")
except Exception as anyError:
    # if anyError == "ValueError":
    #     print("輸入錯誤，請輸入整數數字")
    # else:
    print(f"發生輸入錯誤，類型: {anyError} 發生了")
