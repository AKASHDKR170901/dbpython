def twonumbersum(array,sum):
    nums={}
    for num in array:
        result=sum-num
        if result in nums:
            return[result,num]
        else:
            nums[num]=True
    return[]
