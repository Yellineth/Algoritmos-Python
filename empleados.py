#calcula la retencion de los empleados

n=int(input(" ¿cuantos trabajadores son? "))
for i in range (n):
    codigo=int(input(" ¿cual es el codigo del trabajador? "))
    nh=int(input(" ¿cuantos hijos tiene? "))
    rp=float(input(" ¿cual es su retencion acumulada del mes pasado? "))
    s=float(input(" ¿cual es el salario base? "))
    if nh>1:
        r=(s/s+40)*(nh-2)
        rm=rp+r
        print("Codigo del trabajador:",codigo)
        print("Su retencion del mes es:",r)
        print("Su retencion acumulada es:",rm)
    else:
        re=s/5
        ra=rp+re
        print("Codigo del trabajador:",codigo)
        print("Su retencion del mes es:",re)
        print("su retencion acumulada es:",ra)