#Construa um programa que realiza o sorteio de um número entre 1 e 15
#O usuário terá 3 chances de acertar o valor
#A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado.
#Caso o usuário acerte, dê os parabéns.

#%%

import random

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um número:"))
        
        except ValueError as err:
            print("Valor inválido! Entre com um número entre 1 e 15")
            continue
        
        # if numero_usuario > 15 or numero_usuario < 1:
        if 1 <= numero_usuario <= 15:
            return numero_usuario
            
          
        print("Valor inválido! Digite um número entre 1 e 15")


numero_sorteio = random.randint(1,15)

for i in range(3):

    numero_usuario = get_input()

    if numero_sorteio == numero_usuario:
        print("Parabéns!!")
        break

    elif numero_usuario > numero_sorteio:
        print("Número muito alto. Tente um número menor")

    else:
        print("Número muito baixo. Tente um número maior")

else: 
    print("Suas tentativas acabaram!!")

