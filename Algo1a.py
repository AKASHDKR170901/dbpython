def twonumbersum(array,sum):
    for i in range(len(array)-1):
        a=array[i]
        for j in range(i+1,len(array)):
            b=array[j]
            if a+b==sum:
                return[a,b]
    return[]
