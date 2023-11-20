# 縮排 TAB
# 凸排 Shift+TAB

# 字串切割 split()
# https://www.w3schools.com/python/ref_string_split.asp
# replace(尋找字串, 替換字串)
# 字串切割 split 以特定參數指定字串來切割，不給參數時 預設以空白字元切割
# 目標字串.split(',') 指定 , 為分隔符號
# 開啟檔案 open(filename, '開啟模式', encoding='設定特定編碼方式讀取檔案')
# 資料處理 裝箱 拆箱
filename = 'str1.txt'
n_list, e_list, m_list = [], [], []
f = open(filename, 'r', encoding = 'UTF-8')  # 開啟文字檔 以萬國碼 UTF-8 讀取
最大值 = 0
for s in f:
    s2 = s.replace('\n', '') # 將換行資料串起來
    print(f's2 去除 for 讀到的資料最後面的換行字元: {s2}')
    # ============== 字串 指定分隔字元 切割字串 ==============
    s3 = s2.split()
    print(f's3 將資料分割(以指定字元分割成 list): {s3}')  # ['Tom', '100', '99']
    print(f'{s3[0]} 的英文成績 {s3[1]}')
    print(f'{s3[0]} 的數學成績 {s3[2]}')
    print('====================================')
    # ============== 拆箱 ================================
    n, e, m = s3
    # ==============  資料處理 字串 轉 整數==================
    e = int(e)
    m = int(m)
    # ============== 分流 ================================
    # 若資料量非常巨量 此 拆箱 與 分流 動作 將可能耗盡 電腦記憶體 (越 append list 越大)
    n_list.append(n)  # 加入list
    e_list.append(e)  # 加入list
    m_list.append(m)  # 加入list
    # ============== for 讀取檔案時處理 一次一筆 =============
    if e > 最大值:
        最大值 = e
print(f'英文 最大值: {最大值}')
f.close()
print(f'n_list: {n_list}')
print(f'e_list: {e_list}')
print(f'm_list: {m_list}')
print('====================================')
最大值 = 0
for x in e_list:
    print(f'e_list 目前讀取:  {x}')
    if x > 最大值:
        最大值 = x
print(f"e_list 最大值為: {最大值}")
print('====================================')
最小值 = 101
for x in e_list:
    print(f'e_list 目前讀取:  {x}')
    if x < 最小值:
        最小值 = x
print(f"e_list 最小值為: {最小值}")
print('====================================')
# Python builtins 內建函式方式處理
# https://www.w3schools.com/python/python_ref_functions.asp
print(f'e_list: {e_list}')
e_max = max(e_list)
print(f'e_max: {e_max}')
e_min = min(e_list)
print(f'e_min: {e_min}')
e_len = len(e_list)
print(f'e_len: {e_len}')
e_sum = sum(e_list)
print(f'e_sum: {e_sum}')
e_avg = e_sum / e_len
print(f'e_avg: {e_avg}')
