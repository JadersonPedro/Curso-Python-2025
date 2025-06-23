#Escreva um programa que receba uma lista de números
# do usuário e conte quantas vezes um número
# especifico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.

#%%
lista = [1,2,3,3,1,1,5,6,7,2,4,5]

numero = input("Entre com um numero:")
numero = int(numero)

contador = 0 
for i in lista:
    if i == numero:
        contador += 1

print("Quantidade de", numero, ":", contador)


    
