#calcula el factorial de un numero

f=1
i=1
n=int(input(" ¿cual es el numero? "))
for i in range (n):
    f=f*i
print(" El factorial de",n,"es:",f)