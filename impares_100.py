#calcula el promedio de numeros impares, de un total de 100 numeros

acumulador=0
for i in range (100):
    n=int(input(" ¿cual es el numero? "))
    n1=n % 2
    if n1>0:
        acumulador=acumulador+n
promedio=acumulador/100
print(" El proedio es:",promedio)
    