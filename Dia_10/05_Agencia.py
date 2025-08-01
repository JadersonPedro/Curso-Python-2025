#%%

from random import randint

#%%

class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.cliente = []
        self.caixa = 0
        self.emprestimos = []
    
    def verificar_caixa(self):
        if self.caixa < 100000:
            print(f'Caixa abaixo do nível recomendado. Caixa Atual: R${self.caixa}')
        else:
            print(f'O valor de Caixa está ok. Caixa Atual: R${self.caixa}')
    
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
            print(f'Empréstimo de R${valor} concedido ao CPF {cpf} com juros de {juros * 100}%.')
        else:
            print("Empréstimo não é possível. Dinheiro não disponível em caixa.")
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.cliente.append((nome, cpf, patrimonio))



#%%

# Uso da classe
agencia1 = Agencia("4153000168", "91748375", "1053")
agencia1.caixa = 5000
agencia1.verificar_caixa()

print(agencia1.caixa)
agencia1.emprestar_dinheiro(1500, 6285851756, 0.02)
print(agencia1.emprestimos)

#%%

agencia1.adicionar_cliente("Lira", 39103479857, 10000)
print(agencia1.cliente)

#%%

#AgenciaVirtual
class Agencia_virtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal = 0

    def sacar_paypal(self):
        self.caixa

#AgenciaComum
class Agencia_comum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj,numero=randint(1001, 9999))
        self.caixa = 500000

#AgenciaPremium
class Agencia_Premium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj,numero=randint(1001, 9999))
        self.caixa = 10000000 

    
#%%

agencia_virtual = Agencia_virtual("www.agenciavirtual.com.br", 453000154, 38974000)
agencia_virtual.verificar_caixa()

#%%

agencia_comum = Agencia_comum(24354652343, 243567787)
agencia_comum.verificar_caixa()

#%%

agencia_premium = Agencia_Premium(2676776386, 72827837288)
agencia_premium.verificar_caixa()