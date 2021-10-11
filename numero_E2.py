#calcula el cuadrado de un numero ingresado por teclado

from numbers import Real
from tkinter import N


n=float(input("¿cual es el numero?"))
numero=n*n

if numero > 49:
    print("Resultado fuera de rango")
else:
    print("El cuadrado de",n, "es:",numero)