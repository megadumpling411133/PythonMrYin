# 殷志忠老師(TeacherYin.com)
a = [80,100,90]

最大值 = 0
# 從 a 讀取每一項資料
for x in a:
    print('x', x)
    if x > 最大值:
        最大值 = x
    print('最大值', 最大值)
print('---------------------------')
# 自我挑戰 最小值
最小值 = 101
# 從 a 讀取每一項資料
for x in a:
    print('x', x)
    if x < 最小值:
        最小值 = x
    print('最小值', 最小值)
print('---------------------------')
加總 = 0
# 從 a 讀取每一項資料
for x in a:
    print('x', x)
    加總 += x
    print('加總', 加總)