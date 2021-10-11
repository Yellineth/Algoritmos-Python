#suma los numeros ingresados menores que 100

ac=0
while r==no:
    n=float(input(" ¿cual es el numero? "))
    if n>0 and n<100:
        ac=ac+n
    r=str(input(" ¿desea semar otro valor? "))
print(" La suma de los numeros positivos menores que 100 es:",ac)  
