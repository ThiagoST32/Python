a=80000
b=200000
cont=0
while a<b:
    a=a+(a*3/100)
    b=b+(b*1.5/100)
    cont=cont+1
print ( "A ultrapassa ou iguala a B em %d anos",cont )
