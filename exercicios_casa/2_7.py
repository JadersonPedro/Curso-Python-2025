
fruta = input("Entre com o nome da fruta:")

if fruta == "Pera":
    print ("R$1.25")
elif fruta == "Goiaba":
    print ("R$2.15")
elif fruta == "Abacaxi":
    print ("R$3.20")
elif fruta == "Jaca":
    print ("R$5.80")
elif fruta == "Laranja":
    print ("R$0.65")
elif fruta == "Limão":
    print ("R$1.25")
elif fruta == "Maça":
    print ("R$1.50")
elif fruta == "Banana":
    print("R$2.75")
elif fruta == "Uva":
    print ("R$1.90")

else:
    print ("Entre com uma fruta válida:")

#%%
fruta = input ("Entre com uma fruta:")

frutas = {
    "Pera": "R$1.25",
    "Goiaba": "R$2.15",
    "Abacaxi": "R$3.20",
    "Jaca": "R$5.80",
    "Laranja": "R$0.65",
    "Limão": "R$1.25",
    "Maça": "R$1.50",
    "Banana": "R$2.75",
    "Uva": "R$1.90",
}

if fruta in frutas:
    print (frutas[fruta])
else:
    print("Entre com um valor válido!")


