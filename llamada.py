#determina el valor a pagar por una llamada

m=int(input(" ¿cuantos minutos son? "))
if m<=3:
    print(" La llamada cuesta: 150Bs")
else:
    if m>3 and m<5 :
        v=150 + 50
        print (" La llamada cuesta: ",v)
    else:
        va=((m-5)*30)+200
        print(" La llamada cuesta: ",va)


