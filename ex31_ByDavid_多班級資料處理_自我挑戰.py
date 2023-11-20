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
    cp_list = '''動作選單:
            1. 英文
            2. 數學
            3. 物理
            4. 化學
            9. 結束操作'''
    compareTarget = input(f"{cp_list}請輸入要計算的科目編號: ")
    if compareTarget == 1:
        compareTarget = "e"
    elif compareTarget == 2:
        compareTarget = "m"
    elif compareTarget == 3:
        compareTarget = "p"
    elif compareTarget == 4:
        compareTarget = "c"
    return compareTarget
def 各班成績最大值():
    i = 1
    for s in 輸入處理檔名():
        fileName = s
        print(f"第{i}筆檔案資料處理，檔名{fileName}")
        i += 1
        file = open(fileName, 'r', encoding = 'UTF-8')
        最大值 = 0
        for ss in file:
            s2 = ss.replace("\n", "")
            s3 = s2.replace(",", "")
            s4 = s3.split(" ")
            print(f'資料長度: {len(s4)}')
            if len(s4) < 3:
                print('有學生資料不全，跳過該筆資料!!')
                continue
            print(f's4: {s4}')
            n, e, m = s4
            e = int(e)
            m = int(m)
            # targetSubject = 選擇科目()
            # if targetSubject > 最大值:
            #     最大值 = targetSubject
            if e > 最大值:
                最大值 = e
        ClassName = fileName.replace(".txt", "")
        ClassName = ClassName.replace("st", "")
        print(f'{ClassName} 英文 最大值: {最大值}')
        file.close()
各班成績最大值()