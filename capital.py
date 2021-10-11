#calcula en cuanto tiempo se dobla un capital

c=0
vc=float(input(" ¿cual es el valor del capital? "))
vi=float(input(" ¿cual es el valor del interes? "))
while vc*2==va:
    va=vc*vi/100
    c=c+1
print(" Se demora",c,"años en doblar el valor del capital")