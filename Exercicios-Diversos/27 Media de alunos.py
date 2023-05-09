turmas=int(input("Digite o numero total de turmas:"))
media=0
for i in range (turmas):
    while True:
        alunos=int(input("Digite :o numero total de alunos:"))
        if alunos >=40:
            raise Exception("The number shouldn't be an odd integer")
        break
media= ((i*media)+alunos)/(i+1)
print("A media de alunos em cada sala é de:", media)
