def sortedsquaresarray(array):
    sortedsquares=[0 for _ in array]
    aidx=0
    bidx=len(array)-1
    for idx in reversed(range(len(array))):
        a=array[aidx]
        b=array[bidx]
        if abs(a)>abs(b):
            sortedsquares[idx]=a*a
            aidx+=1
        else:
            sortedsquares[idx]=b*b
            bidx-=1
    return sortedsquares


