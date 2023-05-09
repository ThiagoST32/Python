def clear():
    print("\n")
while True:
 n=1
 total=0 
 while True:
         preco = float(input("Produto {}: R$  e 0 para finalizar!: ".format(n)))
         n += 1
         total += preco
         if preco == 0:
            break
 print("-------------------------------------------")
 print("Total: R$ {:.2f} ".format(total))
 dinheiro = float(input("Dinheiro: R$ "))
 print("Troco: R$ {:.2f} ".format(dinheiro - total))
 print("-------------------------------------------")
 reset=  input("Digite 0 para continuar e 1 para sair!: ")
 if reset=="0":
    clear()
 else:
    print(input("Fim da compra!"))
    break