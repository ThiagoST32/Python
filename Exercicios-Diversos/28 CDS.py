cds=int(input("Digite o total de CDS: "))
valor=0
for i in range (cds):
    preco=float(input("Digite o preço de cada CD:"))
    valor=valor+preco
print(valor)