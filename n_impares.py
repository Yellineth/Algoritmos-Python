#calcula cuantos numeros impares hay en un total de 100 numeros enteros

c=0
for i in range (5):
    n=int(input(" ¿cual es el numero? "))
    n1=n % 2
    if n1<0: 
        c=c+1
print("Hay",c,"numeros impares")