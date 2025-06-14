

numero = input("Entre com um numero inteiro oara calcular a sua raiz quadrada:")

numero = int(numero)

raiz = numero ** (1/2) # ** 0,5
raiz = round(raiz, 4)

print("Raiz quadrada de", numero, "é:", raiz)
