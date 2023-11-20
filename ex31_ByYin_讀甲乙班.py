# 殷志忠老師(TeacherYin.com)
n_list = []
e_list = []
m_list = []

filename = 'st甲班.txt'
f = open(filename, 'r', encoding='UTF-8')  # 開啟文字檔 讀取
for s in f:
    # 刪除字串最後 \n
    s2 = s.replace('\n', '')  # replace(尋找字串,替換字串)
    # 切割字串
    s3 = s2.split(',')  # [名,'英文','數學']
    print('s3', s3, '長度', len(s3))
    if len(s3) != 3:
        print('------資料不全-----')
        continue  # 略過下面未完成程式，迴圈繼續讀取下一筆
    # 拆箱 unpack
    n,e,m = s3
    # 字串 轉 整數
    e = int(e)
    m = int(m)  # 字串 轉 整數
    # 資料分類
    n_list.append(n)
    e_list.append(e)
    m_list.append(m)
f.close()
print('n_list', n_list)
print('e_list', e_list)
print('m_list', m_list)


filename = 'st乙班.txt'
f = open(filename, 'r', encoding='UTF-8')  # 開啟文字檔 讀取
for s in f:
    # 刪除字串最後 \n
    s2 = s.replace('\n', '')  # replace(尋找字串,替換字串)
    # 切割字串
    s3 = s2.split(',')  # [名,'英文','數學']
    print('s3', s3, '長度', len(s3))
    if len(s3) != 3:
        print('------資料不全-----')
        continue  # 略過下面未完成程式，迴圈繼續讀取下一筆
    # 拆箱 unpack
    n,e,m = s3
    # 字串 轉 整數
    e = int(e)
    m = int(m)  # 字串 轉 整數
    # 資料分類
    n_list.append(n)
    e_list.append(e)
    m_list.append(m)
f.close()
print('n_list', n_list)
print('e_list', e_list)
print('m_list', m_list)
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