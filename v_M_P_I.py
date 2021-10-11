#calcula el valor mayor par ingresado y el promedio de los impares, el fin de la serie es el valor centinela -999

import math


m= -math.inf
ac1=0
c1=0
while n==-999:
n=float(input(" ¿cual es el numero? "))
i=n % 2
if n==0:
    print(" Numero no admitido ")
else:
    if i==0 and n>m:
        m=n
    else:
        if i>0:
            ac1=ac1+n
            c1=c1+1
promedio=ac1/c1
print(" El numero mayor par es:",m)
print(" El promedio de los impares es:",promedio)
