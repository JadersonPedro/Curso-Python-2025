#%%

def juros_compostos(anos:int, aporte:int, taxa:float):
        """juros_compostos serve para calcular o retorno financeiro
    a partir de um aporte.
    Deve-se considerar o valor, a taxe de juros e tempo.
    
    aporte:
        um número inteiro, que represente o valor em R$

    taxa:
        um número float entre 0 e 1 que represente o valor da taxa

    anos:
        um número inteiro >=1 que representa o tempo que o investimento terá liquidez.
    
        """
    
        return aporte*(1+taxa) ** anos

#%%

juros_compostos(anos=4, aporte=1000, taxa=0.1)

