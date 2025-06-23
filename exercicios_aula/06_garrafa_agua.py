texto = """Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""
opcao = input (texto)

conta = 0
if opcao == "1":
    conta = 1.5

elif opcao == "2":
    conta = 2.50

if conta == 0:
    print ("Entre com um número válido, por favor")

else:
    print ("Sua conta é: R$" , conta)



