#calcula el jornal diario de unos trabajadores

while r==no:
    nm=str(input(" ¿cual es el nombre del trabajador? "))
    h=float(input(" ¿cuantas horas trabajo? "))
    t=str(input(" ¿En que turno trabajo? "))
    d=str(input(" ¿Que dia de la semana es? "))
    if d=="Domingo" and t=="Diurno":
        j=h*70
        print(" Nombre:",nm)
        print(" El jornal a pagar es de:",j)
    else:
        if d=="Domingo" and t=="Nocturno":
            jo=h*100
            print(" Nombre:",nm)
            print(" El jornal a pagar es de:",jo)
        else:
            if d!="Domingo" and t="Diurno":
                jor=h*50
                print(" Nombre:",nm)
                print(" El jornal a pagar es de:",jor)
            else:
                jorn=h*80
                print(" Nombre:",nm)
                print(" El jornal a pagar es de:",jorn)