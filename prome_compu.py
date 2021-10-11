#calcula el promedio de un curso de computacion con "n" estudiantes

acumulador=0
numero=int(input(" ¿cual es el numero de estudiantes? "))
for i in range (numero):
    nota=float(input(" ¿cual es la nota? "))
    acumulador=acumulador+nota
promedio=acumulador/numero
print(" El promedio es: ",promedio)
