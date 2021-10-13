def isvalidsubsequence(array,sequence):
    seqidx=0
    for value in array:
        if seqidx==len(sequence):
            break
        elif sequence[seqidx]==value:
            seqidx+=1
    return seqidx==len(sequence)