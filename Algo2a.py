def isvalidsequence(array,sequence):
    arridx=0
    seqidx=0
    while arridx<len(array) and seqidx<len(sequence):
        if array[arridx]==sequence[seqidx]:
            seqidx += 1
        arridx += 1
    return seqidx==len(sequence)

