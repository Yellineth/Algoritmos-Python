#calcula la factura de un articulo determinado

ac1=0
ac2=0
ac3=0
nombre=str(input(" ¿cual es el nombre del cliente? "))
fecha=float(input(" ¿cual es la fecha actual? "))
precio=float(input(" ¿cual es el precio de venta? "))
while precio==str:
    n=str(input(" ¿cual es el nombre de el producto?" ))
    iva = (precio*12)/100
    pb=precio+iva
    if pb>150:
        valor=precio-((precio*15)/100)
        ac1=ac1+valor
        print("El valor de ",n,"es:",valor)
    else:
        print("el valor de ", n, "es:",pb)
        ac2=ac2+pb
precio=float(input(" ¿cual es el precio de venta? "))
ac3=(ac3+ac1)+ac2
print("El total a pagar es:",ac3)


