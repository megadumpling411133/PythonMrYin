# 殷志忠老師(TeacherYin.com)

# BMI
# https://depart.femh.org.tw/dietary/3OPD/BMI.htm


# cm = 170
# cm = int(input('輸入身高cm: '))
cm = float(input('輸入身高cm: '))
kg = 70
m = cm / 100
bmi = kg / m ** 2   #  ** 次方
print(cm, kg, bmi)
if bmi < 18.5:
    print('過輕')
# elif bmi >= 18.5 and bmi < 24:
elif 18.5 <= bmi < 24:
    print('正常')
elif 24 <= bmi < 27:
    print('過重')