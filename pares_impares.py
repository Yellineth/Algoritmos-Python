#realiza la suma de los numeros pares e impares de forma independiente de los numeros correspondidos del 1 al 200

ac1=0
ac2=0
for i in range(200):
    numero=i % 2
    if numero==0:
        ac1=ac1+i
    else:
        ac2=ac2+i
print(" La suma de los numeros pares es:",ac1)
print(" La suma de los numeros impares es:",ac2)

