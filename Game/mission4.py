def frequency_count(arr):
    result={}
    for i in arr:
        try:
            if result[i]>=1:
                result[i]+=1
        except:
            result[i]=1

    return result

    
# if i in result (is the another way and it is the good practice )




crystals = [4, 1, 7, 4, 1, 4, 7]
a=frequency_count(crystals)
print(a)