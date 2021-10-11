#calcula la media aritmetica de una lista de numeros negativos terminada con un 0

ac=0
c=0
while n==0:
    n=float(input(" ¿cual es el numero? "))
    if n>0:
        print(" Numero positivo")
    else:
        ac=ac+n
        c=c+1
mA=ac/c
print(" La media aritmetica es:",mA)