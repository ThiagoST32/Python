total_pessoas=int(input("Digite o numero total de pessoas: "))
media=0
for i in range(1, total_pessoas + 1):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    media = ((media * (i - 1)) + idade) / i
if media <26:
    print("Jovem") 
elif media <35:
    print("Adulto")
elif media <60:
    print("Idoso")