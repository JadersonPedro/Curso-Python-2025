#%%

def soma(a:float, b:float, *args)->float:
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args)+2)

a = float(input("entre com o valor de a:"))
b = float(input("entre com o valor de b:"))
c = float(input("entre com o valor de c:"))

print("Média:", media(a,b,c))