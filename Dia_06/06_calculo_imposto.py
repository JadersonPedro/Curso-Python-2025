#%%
def calc_imposto(preco:float, tx_base:float, **kwargs)->float:
    imposto = preco * tx_base
    
    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco*kwargs[i]

    return imposto

#%%

impostos_gerais = {
    "Municipio":0.01,
    "Estadual":0.005,
     "Federal":0.001

}

calc_imposto(100, 0.03, **impostos_gerais)

