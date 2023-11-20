# 殷志忠老師(TeacherYin.com)

# 縮排 TAB
# 凸排 Shift+TAB

# 字串切割 split()
# https://www.w3schools.com/python/ref_string_split.asp

filename = 'st.txt'
f = open(filename, 'r', encoding='UTF-8')  # 開啟文字檔 讀取
# a = []  # list
n_list = []
e_list = []
m_list = []
最大值 = 0
for s in f:
    # 注意 replace() 將取代結果以新字串返回 原本s字串無法修改
    s2 = s.replace('\n', '')  # replace(尋找字串,替換字串)
    print(s2)
    # 字串切割
    #   s2.split(' ') 預設空白為分隔符號
    #   s2.split(',') 指定 , 為分隔符號

    s3 = s2.split()
    print('s3 =', s3)  # ['Tom', '100', '99']
    print('英文成績', s3[1])
    # x = int(s3[1])  # 字串 轉 整數
    # a.append(x)  # 加入list
    # print(a)
    # 拆箱
    n,e,m = s3
    e = int(e)  # 字串 轉 整數
    m = int(m)  # 字串 轉 整數
    print('拆箱', n,e,m)
    n_list.append(n)
    e_list.append(e)
    m_list.append(m)
    # print('n_list', n_list)
    # print('e_list', e_list)
    # print('m_list', m_list)
    if e > 最大值:
        最大值 = e
    print('英文 最大值', 最大值)
f.close()

print('n_list', n_list)
print('e_list', e_list)
print('m_list', m_list)


最大值 = 0
# 從 a 讀取每一項資料
# for x in a:
for x in e_list:
    print('x', x)
    if x > 最大值:
        最大值 = x
    print('最大值', 最大值)
print('-----------------------------')
# pyton 內建函數
# https://www.w3schools.com/python/python_ref_functions.asp
print('e_list', e_list)
e_max = max(e_list)
print('e_max', e_max)
e_min = min(e_list)
print('e_min', e_min)
e_len = len(e_list)
print('e_len', e_len)
e_sum = sum(e_list)
print('e_sum', e_sum)
e_avg = e_sum / e_len
print('e_avg', e_avg)

