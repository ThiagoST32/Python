fatura = {}
fatura["nomeCliente"] = input("Digite o nome do cliente: ")
fatura["diaVenc"] = input("Digite o dia de vencimento: ")
fatura["mesVenc"] = input("Digite o mês de vencimento: ")
fatura["valor"] = input("Digite o valor da fatura: ")
msg = "Olá, {}\nA sua fatura com vencimento em {} de {} no valor de R$ {} está fechada."
print(msg.format(fatura["nomeCliente"], fatura["diaVenc"], fatura["mesVenc"], fatura["valor"]))