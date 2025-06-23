#%%

#uma maneira de definir listas

idades = [28, 42, 43, 35, 39, 28, 38]

print (idades)


#%%

jaderson = ["Jaderson", "Pedro", 35, 2, "Noivo", 3200]

print (jaderson)

#%%

type (jaderson)

#%%

#idade
print (jaderson[2])

#renda
print (jaderson[5])

#nome
print (jaderson[0])

#%%

idades = [28, 42, 43, 35, 39, 28, 38, 42, 34]

print("soma idades:", sum(idades))

print("quantidade idades:", len(idades))

print("media idades:", sum(idades)/ len(idades))

print("menor idade:", min(idades))

print("maior idade:", max(idades))

#%%

jaderson = ["Jaderson Pedro", 35, 
            2, "Noivo",
            ["Estagiário", "Mestrando", "Freela", "Professor"],
             [1000, 1700, 1000, 3500],
             ["Morgana", "Aline"]] 

print("qtde:", len(jaderson))

print("primeira ficante:", jaderson[6][0])

#%%

tamanho = len(jaderson)
pos = tamanho -1
jaderson[pos][1]

ficante = jaderson[pos]

jaderson[pos][len(ficante)-1]

#%%

jaderson[-1][-2]

#%%

#primeiros 4 elementos
jaderson[0:4]

#%%

jaderson[4][-2:]

#%%

salarios = jaderson[5]
salarios [::2]















# %%
