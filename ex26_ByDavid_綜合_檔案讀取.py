# 輸入資料
def inputData():
    name = input("please sign your name here: ")
    try:
        eng = int(input("please enter your english score here: "))
        math = int(input("please enter your math score here: "))
        return (name, eng, math)
    # except ValueError:
    #     print(f'other ValueError happend)
    except Exception as otherError:  # 不建議這樣忽略錯誤
    # 不指定會接住所有其他錯誤

        print(f'其他錯誤: {otherError} 發生了')

# 打包資料
# def packingData([name, eng, name]):
p = inputData()
#
# # 儲存檔案
filename = 'str3.txt'
f = open(filename, "w")
s = f"name: {p[0]} english: {p[1]} math: {p[2]}"
f.write(s)
f.close()
#
# # 讀取資料
print('--- 讀取檔案資料 ---')
f = open(filename, 'r')

for str in f:
    print(str)
f.close()



