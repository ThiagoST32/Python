Candidato1=0
Candidato2=0
Candidato3=0

eleitores=int(input("Numero total de eleitores:"))
for i in range (eleitores):
    voto=int(input("Digite o numero do candidato:"))
    if voto ==1:
        Candidato1=Candidato1+1
    elif voto ==2:
        Candidato2=Candidato2+1
    elif voto==3:
        Candidato3=Candidato3+1
print("Candidato1 total de votos:",Candidato1,"\nCandidato2 total de votos:",Candidato2,"\nCandidato3 total de votos:",Candidato3)

    



