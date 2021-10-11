def sumar(a, b):
    suma=a + b
    return suma

 
n1= int(input("¿cual es el numero 1?"))
n2=int(input("¿cual es el numero 2?"))
resultado = sumar(n1, n2)
print('la suma de {} y {} es igual {}.'.format(n1, n2, resultado))