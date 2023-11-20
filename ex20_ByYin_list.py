# 殷志忠老師(TeacherYin.com)
# list
# https://www.w3schools.com/python/python_lists_loop.asp

# 裝箱 (放資料)
a = ['Tom',100,99]
print(a)
print(type(a))  # type() 查詢資料類型為 list

# 拆箱 (讀資料)
# n = a[0]
# e = a[1]
# m = a[2]
n,e,m = a
print('n =', n)
print('e =', e)
print('m =', m)

print('長度(資料數量)', len(a))

print('最後一項 值', a[-1])
print('最後一項 索引編號', len(a)-1)

i = 1
x = 80
print(f'第{i}項 修改 {x}')
a[i] = x
print(a)

i = 2
x = a.pop(i)  # 刪除(取出)
print(f'第{i}項 取出{x}')
print(a)

x = 90
print('新增', x)
a.append(x)  # 新增
print(a)

print('逐項讀取 for in')
for x in a:
    # 讀到資料要執行的程式
    print(x)