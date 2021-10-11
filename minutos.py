#calcula el valor a pagar segun los minutos
 
from re import M


minutos=int(input("¿cuantos minutos son?"))
if minutos<=3:
    m=minutos*100
    print("el valor a pagar es:" ,m)
else:
    if minutos>=10:
        m1=minutos*100
        m2=(m1*20)/100
        m3=m1-m2
        print("el valor a pagar es:" ,m3)
    else:
        m4=((minutos-3)*50)+300
        print("el valor a pagar es:" ,m4)
    