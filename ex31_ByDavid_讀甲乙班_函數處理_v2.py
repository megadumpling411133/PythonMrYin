def 選擇選項():
    op_list = '''動作選單:
        0. 輸入檔名
        1. 輸入資料
        2. 打包資料
        3. 儲存資料
        4. 讀取資料
        9. 結束操作'''
    while True:
        # 檢查錯誤
        try:
            # 檢查動作編號範圍 1 ~ 5 or 9
            while True:
                op = int(input(f'{op_list}\n請輸入執行動作編號: '))
                if (0 <= op <= 4) or op == 9:
                    if op == 0:
                        action = f"輸入檔名"
                    elif op == 1:
                        action = "輸入資料"
                    elif op == 2:
                        action = "打包資料"
                    elif op == 3:
                        action = "儲存資料"
                    elif op == 4:
                        action = "讀取資料"
                    elif op == 9:
                        action = "結束操作"
                    print(f'條件編號: {op}\n執行動作: {action}')
                    return op
                else:
                    print("請輸入選項範圍: 動作(1 ~ 4) 或是 結束(9) \n請重新輸入")
        # 檢查整數輸入錯誤
        except ValueError:
            print("輸入錯誤，請輸入整數數字")
        # 檢查其他錯誤
        except Exception as err:
            print(f'發生其他錯誤: {err} !!!')
def 輸入處理檔名():
    fileCount = range(int(input('請輸入檔案筆數: ')))
    fileList = []
    for i in fileCount:
        print(f'第 {i + 1} 筆')
        fileList.append(input('請輸入檔案名稱: '))
    print(f'待處理檔案清單: {fileList}')
    return fileList

def 選擇科目():
    cp_list = '''科目選單:
                        1. 英文
                        2. 數學
                        3. 物理(未寫入班級檔案中)
                        4. 化學(未寫入班級檔案中)
                        9. 結束操作\n'''
    while True:
        cp = input(f"{cp_list}請輸入要計算的科目編號: ")
        if cp == "1":
            return "e"
        elif cp == "2":
            return "m"
        elif cp == "3":
            print('物理分數尚未寫入班級檔案中，請重新選擇')
            cp_list = "" # 避免重複顯示選單
            continue
            return "p"
        elif cp == "4":
            print('化學分數尚未寫入班級檔案中，請重新選擇')
            cp_list = "" # 避免重複顯示選單
            continue
            return "c"
        elif cp == "9":
            # print('離開各班成績統計程式!!')
            cp_list = "" # 避免重複顯示選單
            return "out"

def 各班成績統計():
    i = 1   # 從第 1 筆資料開始記數
    科目 = 選擇科目()
    if 科目 == "out":
        print('離開各班成績統計程式!!')
        return
    for s in 輸入處理檔名():
        # 檔案名稱
        fileName = s
        # 班級名稱
        ClassName = fileName.replace(".txt", "")
        ClassName = ClassName.replace("st", "")
        print(f"第 {i} 筆檔案資料處理，檔名{fileName}")
        i += 1  # 計算目前第幾筆
        file = open(fileName, 'r', encoding = 'UTF-8')
        for ss in file:
            s2 = ss.replace("\n", "")
            s3 = s2.replace(",", "")
            s4 = s3.split()
            print(f's4: {s4}')
            if len(s4) < 3: # 資料長度為 科目數量 + 1
                print(f'{ClassName}有學生資料不全，跳過該筆資料!!')
                continue
            n, e, m, p, c= s4
            e = int(e)
            m = int(m)
            n_list.append(n)
            e_list.append(e)
            m_list.append(m)
            if 科目 == "e":
                subject_list = e_list
            elif 科目 == "m":
                subject_list = m_list
            # elif 科目 == "p":
            #     subject_list = p_list
            # elif 科目 == "c":
            #     subject_list = c_list
            最大值 = max(subject_list)
            最小值 = min(subject_list)
            加總值 = sum(subject_list)
            人數值 = len(subject_list)
            平均值 = 加總值/人數值
        print(f'{ClassName} 英文\n最大值: {最大值}\n最小值: {最小值}\n平均值: {平均值}')
        file.close()

n_list = []
e_list = []
m_list = []
# p_list = []
# c_list = []

各班成績統計()