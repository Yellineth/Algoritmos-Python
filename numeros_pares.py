#muestra cuantos numeros pares existen en un conjunto de 120 numeros

from ast import Mod
from operator import mod


np=0
for i in range (120):
    n=int(input(" ¿cual es el numero? "))
    residuo=n % 2
    if residuo==0:
        np=np+1
print("Hay",np,"numeros pares")


