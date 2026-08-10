def check_dulicate(arr):
    seen=[]
    for i in arr:
        if i not in seen:
            seen.append(i)
        else:
            return True
    return False

    pass



crystals = [4, 1, 7]
result=check_dulicate(crystals)
print(result)
