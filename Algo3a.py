def sortedsquarearray(array):
    sortedsquares=[0 for _ in array]
    for idx in range(len(array)):
        value=array[idx]
        sortedsquares[idx]=value*value
    sortedsquares.sort()
    return sortedsquares