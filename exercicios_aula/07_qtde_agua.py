texto = """Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
"""
opcao = input (texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5

elif opcao == "2":
    valor_item = 2.50

if valor_item == 0:
    print ("Entre com um número válido, por favor")


else:
    qtde = input ("Quantas garrafas?")
    qtde = int (qtde)
    valor_total = valor_item * qtde
    print ("Sua conta deu: R$", valor_total)
