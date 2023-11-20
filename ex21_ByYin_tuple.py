# 殷志忠老師(TeacherYin.com)
# tuple 不可修改的list
# https://www.w3schools.com/python/python_tuples.asp

def 產生學生資料list():
    n = input('name:')
    e = int(input('eng:'))
    m = int(input('math:'))
    a = [n,e,m]
    return a

def 產生學生資料tuple():
    n = input('name:')
    e = int(input('eng:'))
    m = int(input('math:'))
    a = (n,e,m)
    return a

# 主流程
# st1 = 產生學生資料list()
# print('st1', st1)
# st1[2] = 9
# print(st1)

st2 = 產生學生資料tuple()
print('st2', st2)
# st2[2] = 9  # 不可修改 引發 TypeError: 'tuple' object does not support item assignment
print(st2)