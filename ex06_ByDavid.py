帳號 = input('請輸入帳號: ')
密碼 = input('請輸入密碼: ')

Br = "\n"
print("帳號: " + 帳號 + Br + "密碼: " + 密碼)

正確帳號 = 'A001'
正確密碼 = '1234'

# Admission 錄取
# Admission_Key_Default = ""
# Admission_Key = Admission_Key_Default
# 判斷是否錄取
Admission_Key = ""
# 帳號驗證
if 帳號 == 正確帳號 and 密碼 == 正確密碼:
    print('登入成功')
    # 輸入成績
    英 = input("請輸入英文分數: ")
    數 = input("請輸入數學分數: ")
    print("英文成績: " + 英 + Br + "數學成績: " + 數)
    英 = int(英)
    數 = int(數)
    # 判斷錄取與否
    if 英 == 0 or 數 == 0:
        print("英文 或 數學 0 分 不錄取")
    elif 英 == 100:
        print("英文滿分 無條件錄取")
        Admission_Key = "Pass"
    elif 英 >= 60 and 數 >= 60:
        print('英文 且 數學 及格 錄取')
        Admission_Key = "Pass"
    if Admission_Key == "Pass":
        # 錄取後計算 BMI
        Height_cm = float(input("請輸入身高(cm): "))
        Weight_kg = float(input("請輸入體重(kg): "))
        Br = "\n"
        # ** 次方運算子
        Height_m = (Height_cm / 100) ** 2
        BMI = Weight_kg / Height_m
        # print(Height_cm, Weight_kg, BMI)
        print("BMI: " + str(BMI))
        if BMI < 18.5:
            print("體重過輕")
        elif 18.5 <= BMI < 24:
            print("體重標準")
        elif 24 <= BMI < 27:
            print("體重過重")
        elif 27 <= BMI < 30:
            print("輕度肥胖")
        elif 30 <= BMI < 35:
            print("中度肥胖")
        elif BMI >= 35:
            print("重度肥胖")
    else:
        if 英 < 60 and 數 < 60:
            print('英文 數學 都不及格 不錄取')
        elif 英 < 60:
            print('英文 不及格 不錄取')
        elif 數 < 60:
            print('數學 不及格 不錄取')
else:
    print('登入失敗 帳號 或 密碼 錯誤')


##### ASCII Code #####
# UserName = input('請輸入帳號: ')
# PassWord = input('請輸入密碼: ')
# Br = "\n"
# print("帳號: " + UserName + Br + "密碼: " + PassWord)
#
# UserName_Certify = 'A001'
# PassWord_Certify = '1234'
#
#
# Admission_Key = ""
#
# if UserName == UserName_Certify and PassWord == PassWord_Certify:
#     print('登入成功')
#
#     Eng = input("請輸入英文分數: ")
#     Mat = input("請輸入數學分數: ")
#     print("英文成績: " + Eng + Br + "數學成績: " + Mat)
#     Eng = int(Eng)
#     Mat = int(Mat)
#
#     if Eng == 0 or Mat == 0:
#         print("英文 或 數學 0 分 不錄取")
#     elif Eng == 100:
#         print("英文滿分 無條件錄取")
#         Admission_Key = "Pass"
#     elif Eng >= 60 and Mat >= 60:
#         print('英文 且 數學 及格 錄取')
#         Admission_Key = "Pass"
#     if Admission_Key == "Pass":
#
#         Height_cm = float(input("請輸入身高(cm): "))
#         Weight_kg = float(input("請輸入體重(kg): "))
#         Br = "\n"
#
#         Height_m = (Height_cm / 100) ** 2
#         BMI = Weight_kg / Height_m
#         # print(Height_cm, Weight_kg, BMI)
#         print("BMI: " + str(BMI))
#         if BMI < 18.5:
#             print("體重過輕")
#         elif 18.5 <= BMI < 24:
#             print("體重標準")
#         elif 24 <= BMI < 27:
#             print("體重過重")
#         elif 27 <= BMI < 30:
#             print("輕度肥胖")
#         elif 30 <= BMI < 35:
#             print("中度肥胖")
#         elif BMI >= 35:
#             print("重度肥胖")
#     else:
#         if Eng < 60 and Mat < 60:
#             print('英文 數學 都不及格 不錄取')
#         elif Eng < 60:
#             print('英文 不及格 不錄取')
#         elif Eng < 60:
#             print('數學 不及格 不錄取')
# else:
#     print('登入失敗 帳號 或 密碼 錯誤')