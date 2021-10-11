#suma los numeros impares menores que 100 y calcula su promedio

ac=0
c=0
i=0
for i in range (100):
    r=i % 2
    if r!=0:
        ac=ac+i
        c=c+1
promedio=ac/c
print(" La suma de los numeros positivos menores que 100 es:",ac)
print(" El promedio de los numeros impares menores que 100 es:",promedio)
