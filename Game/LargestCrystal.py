crystals = [5, 12, 3, 25, 8]

HighestCrytal = crystals[0]
LowestCrytal = crystals[0]

for i in crystals:
    if HighestCrytal<i:
        HighestCrytal=i
    if LowestCrytal>i:
        LowestCrytal=i 


print(f'Higest Crystal - {HighestCrytal} || Lowest Crystal - {LowestCrytal}')