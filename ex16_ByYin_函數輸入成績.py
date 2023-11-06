# 殷志忠老師(TeacherYin.com)
def 輸入英文成績():
    while True:
        eng = int(input('請輸入英文成績(0~100):'))
        if eng < 0 or eng > 100:
            print('輸入錯誤，成績必須 0 ~ 100 之間')
        else:
            # break
            return eng

eng = 輸入英文成績()
print('eng', eng)