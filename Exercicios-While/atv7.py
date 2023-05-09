A = 1000
ano = 1996
atual = int(input("Digite o ano em que estamos: "))
aum = 0.015
cont = atual - ano

while ano < atual:
    salario = A + (A * (aum * (2**cont)))
    ano = atual
print("O salário atual do moço é: ", salario)