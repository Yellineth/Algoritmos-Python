#calcula uno de los catetos de un triangulo
import math
from numbers import Real


c1=float(input("¿cual es el valor de el primer cateto?"))
h=float(input("¿cual es el valor de la hipotenusa?"))
c2=((h*h)-(c1*c1))
c= math.sqrt(c2)
print("El valor del otro cateto es de :",c)