from array import array
 

v=[8,6,3,8,2,4,5,2,2,15,10
]
sum=0
tamano= len(v)

for i in range(0,tamano):

    sum=sum +v[i]

media=round (sum/tamano)

aux=[]
for i in range(0,tamano):
  
  if(v[i]<=media):
        
aux.append(v[i])
print(aux)
