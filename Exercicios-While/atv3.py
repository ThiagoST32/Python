nome=str(input("Digite seu nome: ")).casefold()
while ( len(nome) <=  3 ):
	nome=str(input("informe um nome--> "))

idade=int(input("Digite sua idade: "))
while (idade >150 or idade <=0):
    idade=int(input("Digite sua idade: "))


salario=float(input("Digite seu salario: "))
while (salario < 0):
    salario=float(input("Digite sua salario: "))

sexo=str(input("Digite seu Sexo: ")).casefold()
while sexo != "feminino" and sexo != "masculino":
    sexo=str(input("Digite seu sexo: "))

civil=str(input("Digite seu estado civil: ")).casefold()
while (civil != "solteiro" and civil != "Casado" and civil != "Divorciado"):
    civil=str(input("Digite seu estado civil: "))
