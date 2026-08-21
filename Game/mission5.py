def most_frequent(arr):
    result={}
    max_count=0
    max_n=None
    for i in arr:

        try:
            if result[i]>=1:
                result[i]+=1

        except:
            result[i]=1
        if result[i]>max_count:
          max_count=result[i]
          max_n=i


    return max_n




crystals = [7, 7, 4, 4, 4]
a=most_frequent(crystals)
print(a)