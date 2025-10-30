# Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

# Nome do produto: "Cadeira Infantil"
# Preço unitário: R$ 12.40
# Quantidade: 3 
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.


nome_produto = "Cadeira Infantil"
preco_uni = 12.40
quantidade= 3

preco_total = preco_uni * quantidade

print("#- Preço total da compra -#")
print(f"Produto: {nome_produto}")
print(f"Preço unitário: {preco_uni}")
print(f"Quantidade: {quantidade}")
print("##########################")
print(f"Valor total da compra: {preco_total}")