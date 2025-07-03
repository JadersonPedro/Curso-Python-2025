#%%

import requests     #para realizar requisições na web
import json         #para tratar json de listas/dicionários para arquivos 
from tqdm import tqdm

import pandas as pd

#%%
ceps = [
    "80010150",
    "80050510",
    "13180000",
    "13185000",
    "96205210",
    "96207650",
    "96205160", 
]

url = "http://viacep.com.br/ws/{cep}/json/"
dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

#%%

dataset = pd.DataFrame(dados)
dataset

#%%

with open("ceps.json", "w") as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)

