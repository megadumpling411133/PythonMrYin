# 呼叫函數

# input( 提示訊息 )   # 輸入資料 一律以文字資料處理
# 此函數 將輸入資料以字串處理
Name = input('Please Sign Your Name Here: ')
print('Welecome', Name)

Eng = input('Please Enter Your English Score Here: ')
Mat = input('Please Enter Your English Score Here: ')
Total = Eng + Mat
print('Total Score: ' +  Total)

# int() 整數功能 調整為整數的小幫手
Format_Total = int(Eng) + int(Mat)
print('Total Score:', Format_Total)
Mean = Format_Total / 2
Mean = str(Mean)
Break = "\n"

# 下方的換行也能執行 可能是 IDE 做的
print("Name: " + Name + Break,
      "English Score: " + Eng + Break,
      "Math Score" + Mat + Break,
      "Total Score: " + Total + Break,
      "Mean Score: " + Mean)

