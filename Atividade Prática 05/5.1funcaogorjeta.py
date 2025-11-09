def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:

    if valor_conta < 0 or porcentagem_gorjeta < 0:
        return 0.0  

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

total_conta = 120.50
percentual = 18
valor_gorjeta = calcular_gorjeta(total_conta, percentual)
print(f"Conta: R$ {total_conta:.2f}")
print(f"Gorjeta ({percentual}%): R$ {valor_gorjeta:.2f}")
print(f"Total a pagar: R$ {total_conta + valor_gorjeta:.2f}")