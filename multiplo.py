#calcula si un numero es multiplo del otro ingresados 2 numeros

n1=int(input(" ¿cual es el primer numero? "))
n2=int(input(" ¿cual es el segundo numero? "))
m=n2 % n1
if m==0:
    print(n2,"es multiplo de",n1)
else:
    print(n2,"no es multiplo de",n1)