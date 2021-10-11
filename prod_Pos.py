#calcula el producto de los numeros positivos comprendidos desde el -500 hasta el 2000

i=-500
acn=0
acp=0
for i in range (2000):
    if i<0:
        acn=acn*i
    else:
        acp=acp*i
print(" El producto de los numeros positivos es:",acp)
print(" El producto de los numeros negativos es:",acn)