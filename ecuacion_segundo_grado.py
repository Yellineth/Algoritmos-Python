#calcula las raices de una ecuacion de segundo grado
 
import math
a=float(input(" ¿cual es el valor de a? "))
b=float(input(" ¿cual es el valor de b? "))
c=float(input(" ¿cual es el valor de c? "))
x0=((b*b)-(4*a*c))
x= math.sqrt(x0)
if x < 0 :
    print(" La ecuacion no existe ")
else:
    if x > 0 :
        x1=(-b+x)/2
        x2=(-b-x)/2
        print("La primera raiz de la ecuacion es:",x1)
        print("La segunda raiz es:",x2)