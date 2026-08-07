crystals = [2, 7, 11, 15]
target = 9

for i in range(len(crystals)):
    for j in range(i+1,len(crystals)):
        if crystals[i]+crystals[j]==target:
            print(i,j)