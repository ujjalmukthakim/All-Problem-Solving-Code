def check_dulicate(arr):
    seen=set()
    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            return True
    return False

    



crystals = [4, 1, 7,4]
result=check_dulicate(crystals)
print(result)
