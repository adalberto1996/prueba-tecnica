from array import array


v=[8,6,3,8,2,4,5,2,2,15,10]


tamano= len(v)

primo=[]

bandera=False

def es_primo(num):

    for n in range(2, num):

        if num % n == 0:

            return False

    return True

for i in range(0,tamano):

   if(es_primo(v[i]) == True):

       primo.append(v[i])

sum=0
for j in range(0, len(primo)):

     sum=sum +primo[j]

primos = list(dict.fromkeys(primo))

media=round (sum/len(primos))

  
print(media)
