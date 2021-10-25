from array import array

v=[8,6,3,8,2,4,5,2,2,15,10]



tamano= len(v)
cmoda=0
moda=0
for i in range(0,tamano):
    aux=1
    for j in range(i, tamano):
        if(v[i]==v[j]):
            aux=aux+1
    if(cmoda<aux):
        moda=v[i]
        cmoda=aux

print(moda)
