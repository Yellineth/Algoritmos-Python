#calcula el valor mayor y la suma de una serie de numeros positivos terminada con un numero negativo

m=0
ac1=0
while n>0:
    n=float(input(" ¿cual es el numero? "))
    if n>m:
        m=n
    ac1=ac1+n
print(" El mayor de los numeros es",m)
print(" La suma de los numeros es",ac1)

