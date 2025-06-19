
saldo_total = 0

while True: 
    saldo = input ("Entre com o saldo:")
    if saldo == "":
        break

    saldo_total += float(saldo)

print ("Saldo_total:", saldo_total)
