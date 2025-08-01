#%%

class tv:
    def __init__(self):
        self.cor = "preta"
        self.ligada = False
        self.tamanho = 55
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
    

#%%
tv_sala = tv()
tv_quarto = tv()

tv_sala.cor = "branca"
tv_quarto.tamanho = "32"

print(tv_sala.tamanho)
print(tv_quarto.tamanho)
        
#%%

tv_sala = tv()
tv_quarto = tv()

tv_sala.mudar_canal("Globoplay")
tv_quarto.mudar_canal("Amazon")

print(tv_sala.canal)
print(tv_quarto.canal)

#%%

