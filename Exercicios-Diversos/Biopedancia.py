print ("Cadastro  geral do Usuario")
Nome=(input("Digite seu nome:"))
Sexo=(input("Digite seu sexo:"))
Idade=float(input("Digite sua idade:"))
Telefone=(input("Digite seu Telefone:"))
CPF=float(input("Digite seu CPF:"))
CEP=float(input("Digite seu CEP:"))
Endereço=(input("Digite seu endereço:"))
Nasc=(input("Digite sua data de nascimento:"))
peso=float(input("Digite seu Peso:"))
altura=float(input("Digite sua altura:"))

print("Nome:",Nome)
print("Idade:",Idade)
print("Telefone:",Telefone)
print("CPF:",CPF)
print("CEP:",CEP)
print("Endereço:",Endereço)
print("Data de nascimento:", Nasc)
print("Peso:",peso)
print("Altura:", altura)


imc=(peso/(altura*altura))
if imc <16:
    print("Magreza leve!")
elif imc <17:
    print("Magreza Moderada!")
elif imc <18.5:
    print ("Magreza Leve!")
elif imc <25:
    print("Saudavel!")
elif imc <30:
    print("Sobre peso!")
elif imc <35:
    print ("Obesidade grau I!")
elif imc <40:
    print ("Obesidade grau II!(Severa)")
elif imc <45:
    print ("Obesidade grau III!(Grave)")

print("Seu IMC é: %.2f" % imc)
MG=float(1.20*imc)+(0.23*Idade)-(10.8*1)-5.4
MG2=float(1.20*imc)+(0.23*Idade)-(10.8*0)-5.4
if Sexo=="Masculino":
    MG=float(1.20*imc)+(0.23*Idade)-(10.8*1)-5.4
elif Sexo=="Feminino":
    MG2=float(1.20*imc)+(0.23*Idade)-(10.8*0)-5.4
print("Sua Massa Gorda é:" "%.2f" % MG)
aguaC = (35*peso)
aguaL = (aguaC/1000)
print("Sua Agua Coporal é:", aguaL)
MM=(0.32810 * peso) + (0.33929 * altura) - 29.5336
MF=(0.32810 * peso) + (0.33929 * altura) - 29.5336
if Sexo =="Masculino":
    (0.32810 * peso) + (0.33929 * altura) - 29.5336
    print("Sua massa magra é de:""%.2f" % MM)  
elif Sexo=="Feminino":
    (0.29569 * peso) + (0.41813 * altura) - 43.2933
    print("Sua massa magra é de:""%.2f" % MF)







