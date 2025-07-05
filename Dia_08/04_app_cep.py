import streamlit as st

import pandas as pd

import requests

url = "http://viacep.com.br/ws/{cep}/json/"

st.title("Busca CEP")

cep = st.text_input("Busque o seu CEP")

if cep != "":
    resp = requests.get(url.format(cep=cep))
    data = pd.DataFrame([resp.json()])
    st.dataframe(data)

