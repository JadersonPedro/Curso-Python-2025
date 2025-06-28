#%%

lista = [2, 132, "Jaderson", ["freela", "mestrado", "professor"], True]

lista [2]

#%%

# Lista = pares de chave/valor

dados_jaderson = {
    "sobrenome":"Costa",
    "nome":"Jaderson",
    "filhos":True,
    "formacao": ["engenhariaquimica", "bigdata"],
    "cargos": [
        {"cargo": "freelancer", "empresa": "Bauhaus"},
        {"cargo": "mestrando", "empresa": "UFPR"},
        {"cargo": "professor", "empresa": "Aulas particulares de italiano"},
        ]


    
}

print(dados_jaderson)

#%%

print(dados_jaderson["formacao"] [-1])
print(dados_jaderson["cargos"] [0]["empresa"])

#%%

print(dados_jaderson["cargos"] [1] ["empresa"])

#%%

dados_jaderson["estado civil"] = "noivo"

#%%

print("Chaves:", dados_jaderson.keys())

print("Valores:", dados_jaderson.values())

print("Itens:", dados_jaderson.items())

#%%

for i in [10, 20, 45, 28, "Jaderson"]:
    print(i)

#%%

for i in dados_jaderson:
    print(i, "->", dados_jaderson[i])

#%%

for chave, valor in dados_jaderson.items():
    print(chave, "->", valor)
