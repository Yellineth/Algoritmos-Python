#calcula el promedio de notas de un curso de computacion


cr=0 
ca=0
accumulate=0
na=int(input("¿cuantos alumnos son?"))

for i in range(na):
    n=float(input(" ¿cual es la nota? "))
    accumulate=accumulate+n
    if n<50:
        cr=cr+1
    else:
        ca=ca+1
promedio=accumulate/na
print("El promedio del curso es:",promedio)
print("El numero de estudiantes reprobados es",cr)
print("El numero de estudiantes aprobados es",ca)

