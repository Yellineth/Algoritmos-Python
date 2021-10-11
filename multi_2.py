#suma y cuenta los multiplos de 2 de un conjunto de 300 numeros enteros

acumulador=0
m=0
for i in range(5):
    numero=int(input(" ¿cual es el numero? "))
    n=numero % 2
    if n==0:
        acumulador=acumulador + numero
        m=m+1
print(" La suma de los multiplos de 2 es",acumulador)
print(" Ingreso:",m,"numeros que son multiplos de 2")