#calcula el valor mayor de una serie de numeros"n" conociendo el rango entre -32768 y32367

mayor=0
n=int(input(" ¿cuantos numeros son?"))
for i in range (n):
    nm=float(input(" ¿cual es el numero? "))
    if nm>-32768 and nm<32767:
        if nm>mayor:
            mayor=nm
print("El mayor valor ingresado fue:",mayor)
