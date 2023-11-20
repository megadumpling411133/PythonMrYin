def 輸入學生資料_list():
    name = input("please enter student name: ")
    eng = input("please enter English score: ")
    math = input("please enter Math score: ")

    list_st = [name, eng, math]
    return list_st


def 輸入學生資料_tuple():
    # tuple() 資料不可竄改 更安全
    name = input("please enter student name: ")
    eng = input("please enter English score: ")
    math = input("please enter Math score: ")

    tuple_st = (name, eng, math)
    return tuple_st

# 主流程
# st1 = 輸入學生資料_list()
# print(f"學生輸入的資料內容: {st1}")
# st1[2] = 50 # list 可被修改(竄改)
# print(f"學生被竄改資料內容: {st1}")
# print(st1)

st2 = 輸入學生資料_tuple()
# print(f"學生輸入的資料內容: {st2}")
name, eng, math = st2
print(f'學生輸入的資料如下:\n學生姓名: {name}\n英文成績: {eng}\n數學成績: {math}')
# st2[2] = 50 # list 可被修改(竄改)     # TypeError: 'tuple' object does not support item assignment
# print(f"學生被竄改資料內容: {st2}")
# print(st2)

# st1 = 輸入學生資料_list()
# name, eng, math = st1
# print(f'學生輸入的資料如下:\n學生姓名: {name}\n英文成績: {eng}\n數學成績: {math}')
# st1[2] = 50 # list 可被修改(竄改)
# name, eng, math = st1
# print(f'學生被竄改的資料如下:\n學生姓名: {name}\n英文成績: {eng}\n數學成績: {math}')