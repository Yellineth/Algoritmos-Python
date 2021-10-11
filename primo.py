#calcula si un numero es primo o no

c=0
n=int(input(" ¿cual es el numero? "))
for i in range (n):
    m= n % i
    if m==0:
        c=c+1
if c>0:
    print(" El numero no es primo")
else:
    print (" El numero es primo")