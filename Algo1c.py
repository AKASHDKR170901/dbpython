def twonumbersum(array,sum):
    array.sort()
    left=0
    right=len(array)-1
    while left<right:
        n=array[left]+array[right]
        if n==sum:
            return[array[left],array[right]]
        elif n<sum:
            left+=1
        elif n>sum:
            right-=1
    return[]
