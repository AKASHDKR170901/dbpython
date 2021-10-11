import copy
l1=[10,20,[30,40],50]
l2=copy.deepcopy(l1)
l1[0]=111
l2[1]=222
l1[2][0]=888
l1[2][1]=999
l1[3]=777
print(l1)
print(l2)

