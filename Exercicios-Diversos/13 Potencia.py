
num=int(input("Digite o valor:"))
exponent=int(input("Digite o Expoente:"))
portencia=1
for i in range (exponent):
    portencia*=num
print (num,"^",exponent,"=",portencia)
