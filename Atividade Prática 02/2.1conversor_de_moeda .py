# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.60
# Taxa do euro: R$ 6.60 
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

taxaDolar = 5.60
taxaEuro = 6.60
valoremReais = 100


realeuro = (valoremReais / taxaEuro)
realdolar = (valoremReais / taxaDolar)

print(f"A Converção de Real para Euro:{realeuro:.2f}")
print(f"A Converção de Real para Dólar:{realdolar:.2f}")