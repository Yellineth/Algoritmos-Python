#calcula el valor mayor de una serie de numeros q termina con el valor centinela -99
import math


m= -math.inf
while n==-99:
    n=float(input(" ¿cual es el numero? "))
    if n==0:
        print(" Numero no admitido ")
    else:
        if n>m:
            m=n
print(" El numero es:",m)