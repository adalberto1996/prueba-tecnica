from array import array

def verificar(secuencia,tsecuencia, numinse, ban):
    j = 0
    k = tsecuencia-1
    if(tsecuencia%2==0):
        mitad1=round(tsecuencia/2)-1
        mitad2=round(mitad1+1)
        while( (j<=mitad1) and (k>=mitad2)):
            if(secuencia[j]==secuencia[k]):
                j=j+1
                k=k-1
            else:
                secuencia.insert(k+1,  secuencia[j])
                ban = True
                return secuencia, len(secuencia), numinse+1, ban
        ban = True
        return secuencia, len(secuencia), numinse, ban
    else:
        mitad=round(tsecuencia/2)
        while( (j<mitad) and (k>mitad)):
            if(secuencia[j]==secuencia[k]):
                j=j+1
                k=k-1
            else:
                secuencia.insert(k+1,  secuencia[j])
                ban = True
                return secuencia, len(secuencia), numinse+1, ban
        ban = False
        return secuencia, len(secuencia), numinse, ban


nsecuencia=input()
nsecuencia=int(nsecuencia)
for i in range(0, nsecuencia):
    tsecuencia=input()
    tsecuencia=int(tsecuencia)
    separador = " "
    numinse=0
    bandera=True
    cadena=input()
    secuencia = cadena.split(separador, tsecuencia-1)
    secuencia = list(map(int, secuencia))
    while bandera == True:
        secuencia, tsecuencia, numinse, bandera = verificar(secuencia, tsecuencia, numinse, bandera)
    print("secuencia #",i+1,":", numinse)
