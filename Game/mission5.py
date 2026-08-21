def most_frequent(arr):
    result={}
    for i in arr:
        max_count=0
        max_n=None
        try:
            if result[i]>=1:
                result[i]+=1

        except:
            result[i]=1
        if result[i]>max_count:
          max_count=result[i]
          max_n=i


    return max_n




crystals = [4, 1, 7, 4, 1, 4, 7, 7, 7]
a=most_frequent(crystals)
print(a)