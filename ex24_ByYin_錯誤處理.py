# 殷志忠老師(TeacherYin.com)

def 測試1():
    try:
        # 想執行但可能發生錯誤的程式
        e = int(input('請輸入英文成績: '))
        # 上一行出錯，下面程式會被略過，跳套錯誤處理
        # x = e / 0  # ZeroDivisionError: division by zero
        print('輸入完成')
    except ValueError:
        # ValueError 錯誤處理程式
        print('錯誤: 請輸入整數數字格式')
    # except:
        # 其他錯誤處理程式
        # print('其他錯誤 發生了')
    print('END')

def 輸入英文成績():
    while True:
        try:
            e = int(input('請輸入英文成績: '))
            return e
        except ValueError:
            print('錯誤: 請輸入整數數字格式')

# 測試1()
x = 輸入英文成績()
print(f'x = {x}')