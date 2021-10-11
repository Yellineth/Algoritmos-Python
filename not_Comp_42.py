#calcula el promedio de notas de un curso de computacion con 42 estudiantes

acumulador=0
for i in range (42):
    nota=float(input(" ¿cual es la nota? "))
    acumulador=acumulador+nota
    promedio=acumulador/42
print(" El promedio del curso es: ",promedio)