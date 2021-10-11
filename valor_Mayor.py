# calcula el mayor valor ingresado de 3 numeros

from asyncio.windows_events import INFINITE
from cmath import inf
from http.client import INSUFFICIENT_STORAGE
import math


mayor=-math.inf
for i in range (3):
    numero=float(input(" ¿cual es el numero? "))
    if numero > mayor :
        mayor=numero
print(" El numero mayor es: ",mayor)        