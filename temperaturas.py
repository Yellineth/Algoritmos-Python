#calcula un par de temperaturas diarias

import math


acMaximo=0
acMinimo=0
ctm=0
maximo=-math.inf
ce=0
cg=0
temperatura1=float(input(" ¿cual es la temperatura maxima? "))
temperatura2=float(input(" ¿cual es la temperatura minima? "))
while temperatura1 !=0 and temperatura2!=0:
    if temperatura1==9 or temperatura2==9:
        print(" Temperatura no permitida ")
        ce=ce+1
    else:
        acMaximo= acMaximo + temperatura1
        acMinimo= acMinimo + temperatura2
        promedio=(temperatura1+temperatura2)/2
        print(" El promedio de este dia es:", promedio)
    if temperatura1>maximo:
        maximo=temperatura1
        ctm= 1
    else:
      if temperatura1==maximo:
          ctm=ctm + 1
    temperatura1=float(input(" ¿cual es la temperatura maxima? "))
    temperatura2=float(input(" ¿cual es la temperatura minima? "))
pe= ce * 100 / cg
porcentajeMaximo= acMaximo / cg
porcentajeMinimo= acMinimo / cg
print("La temperatura maxima fue:",maximo,"y se presento:",ctm,"veces")
print("El porcentaje de errores fue:",pe,"%")
print("El porcentaje de temperaturas maximas es:",porcentajeMaximo,"%")
print("El porcentaje de temperaturas minimas es:", porcentajeMinimo,"%")

    




