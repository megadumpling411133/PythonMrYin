# 習慣 i 從 0 開始計算
# 好處 > while 條件撰寫時較直觀
# i < 3 跑 3 圈操場
# i < 5 跑 5 圈操場
i = 0
print('while loop 之前 i: ', i)
print('-------------')
while i < 3:
    print(i)
    i += 1
print('-------------')
print('while loop 之後 i: ', i)