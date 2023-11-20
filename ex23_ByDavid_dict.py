# dict
# Python 3.7 後 有序
# 由 {key1 : value1, key2 : value2} 組成
# key 唯一不重複: 用來查詢(就像 index 一樣: index 用整數來查詢)
# Value 可重複: 用來存放資料

def T1():
    a = {0: "Davies", 1: "100", 2: "80"}
    print(type(a))
    print(a)
    # 有序 資料會依照建立的方式(順序)排列，當資料被建立，順序就固定了
    name = a[0]
    eng = a[1]
    math = a[2]
    # 查詢時用 key return value
    print(name, eng, math)

# key 直接放字串 才方便查詢
def T2():
    a = {'name': "Davies", 'eng': "100", 'math': "80"}
    print(type(a))
    print(a)
    # 有序 資料會依照建立的方式(順序)排列，當資料被建立，順序就固定了
    name = a['name']
    eng = a['eng']
    math = a['math']
    print(f'查詢目標姓名: {name}, 英文成績: {eng}, 數學成績: {math}')

# 產生學生資料    # 用變數來放入值
def genData_student():
    # 用變數來放入值
    name = input('please enter your name: ')
    eng = int(input('please enter your eng score: '))
    math = int(input('please enter your math score: '))
    # 裝箱於字典 packing
    dict_stData = {'name': name,'eng': eng,'math': math,}
    return dict_stData

# 主流程
# T1()
# T2()
st1 = genData_student()
print(type(st1))
print(st1)
# Python is case sensitive
# print('讀取數學成績', st1['MATH'])  # KeyError: 'MATH'
print(f"讀取數學成績: {st1['math']}")
# 對字典內 key 做操作
st1['math'] = 80    # 若查詢到 key ,會修改 value
print(f'查詢並修改數學成績: {st1}')
st1['Python'] = 99  # 若查詢不到 key ,會新增一筆資料
print(f'查詢並新增 python 成績: {st1}')

key = input('查詢, 請輸入 key 值: ')

if key in st1:
    print(f'查詢 {key}, 其值為 {st1[key]}')
else:
    print(f'查詢 {key}, 查無資料')