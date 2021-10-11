#determina si un numero mayor que 10 es primo o compuesto

c=0
n=int(input(" ¿cual es el numero? "))
if n>10:
    for i in range (n):
        if n % i==0:
            c=c+1
    if c>2:
        print(" El numero es compuesto")
    else:
        print(" El numero es primo")
else:
    print(" El numero no es admitido")