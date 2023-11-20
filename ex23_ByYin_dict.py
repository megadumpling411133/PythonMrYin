# 殷志忠老師(TeacherYin.com)
# dict
# https://www.w3schools.com/python/python_dictionaries.asp

def 測試1():
    a = {0: 'Tom', 1: 100, 2: 99}
    print(type(a))
    print(a)
    n = a[0]
    e = a[1]
    m = a[2]
    print(n,e,m)


def 測試2():
    a = {'name': 'Tom', 'eng': 100, 'math': 99}
    print(type(a))
    print(a)
    n = a['name']
    e = a['eng']
    m = a['math']
    print(n, e, m)

def 產生學生資料dict():
    n = input('name:')
    e = int(input('eng:'))
    m = int(input('math:'))
    a = {'name': n, 'eng': e, 'math': m}
    return a


# 測試1()
# 測試2()
st1 = 產生學生資料dict()
print(type(st1))
print(st1)
# print('讀取數學成績', st1['MATH'])  # KeyError: 'MATH'
print('讀取數學成績', st1['math'])
st1['math'] = 80    # key 存在 即 修改
print(st1)
st1['python'] = 99  # key 不存在 即 新增
print(st1)
k = input('查詢，請輸入 key: ')
if k in st1:
    print(st1[k])
else:
    print('查無資料')