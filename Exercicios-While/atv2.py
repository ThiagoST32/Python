usuario=str(input("Insira seu nome: "))
senha=str(input("Insira sua senha: "))
while usuario==senha:
    print("Erro, Digite novamente: ")
    break
else:
    print("Logado")
    