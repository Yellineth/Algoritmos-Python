#calcula el promedio de numeros negativos de una serie de numeros enteros

ac1=0
c1=0
while n<0:
    n=int(input(" ¿cual es el numero? "))
    residuo=n % 2
    if n<0 and residuo==0:
        ac1=ac1+n
        c1=c1+1
promedio=ac1/c1
print(" El promedio de los numeros pares negativos es:",promedio)