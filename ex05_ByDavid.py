# BMI
# https://depart.femh.org.tw/dietary/3OPD/BMI.htm

# cm = 170
# cm = int(input('輸入身高cm: '))
# cm = float(input('輸入身高cm: '))
# kg = 70
# m = cm / 100
# bmi = kg / m ** 2   #  ** 次方
# print(cm, kg, bmi)
# if bmi < 18.5:
#     print('過輕')
# # elif bmi >= 18.5 and bmi < 24:
# elif 18.5 <= bmi < 24:
#     print('正常')
# elif 24 <= bmi < 27:
#     print('過重')


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
elif 24 <= BMI < 27 :
    print("體重過重")
elif 27 <= BMI < 30:
    print("輕度肥胖")
elif 30 <= BMI < 35:
    print("中度肥胖")
elif BMI >= 35:
    print("重度肥胖")

# print("身高(公分): " + str(Height_cm) + Br +
#       "體重(公斤): " + str(Weight_kg) + Br +
#       "BMI: " + BMI)
