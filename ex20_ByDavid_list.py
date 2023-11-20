# list

# 裝箱(程式術語) packing(Python) boxing(JAVA)
list_A = ["David", 100, 99]
print(list_A)
print(type(list_A))     # type() 查詢資料類型為 list

# 拆箱 unpacking unboxing
# n = list_A[0]
# e = list_A[1]
# m = list_A[2]
name, eng, math = list_A    # 多值拆箱 存入變數
print('name =', name)
print('eng =', eng)
print('math =', math)
# scare brackets 方括號內放 index 從 0 開始
# index 從 0 開始
# length 從 1 開始
print('長度(資料數量)', len(list_A))
print('最後一項 值', list_A[-1])
print('最後一項 索引編號', len(list_A)-1)

i = 1
x = 80
print(f'修改第{i}項(index{i}) 修改 {x}')
list_A[i] = x
print(list_A)

i = 2
x = list_A.pop(i)  # 刪除(取出指定項)
print(f'第{i}項 取出 {x}')
print(list_A)

# append Method 加在最後一 "項"
x = 90
print('新增', x)
list_A.append(x)  # 新增()
print(list_A)
# b 被 append 在 a 的第 4 項
# a = ["a", "b", "c"]
# b = ["d", "e", "f"]
# a.append(b)
# print(a)           # ["a", "b", "c", ["d", "e", "f"]]

print('逐項讀取 可迭代物件 for in')
# 逐項讀取 可迭代物件(這裡為 list)存入變數中(這裡為 x)
for x in list_A:
    # 讀到資料要執行的程式
    print(x)









