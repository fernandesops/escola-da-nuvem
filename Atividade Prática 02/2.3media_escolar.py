# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
# Nota 1: 7.5
# Nota 2: 8.0
# Nota 3: 6.5 
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

n1 = 7.5
n2 = 8.0
n3 = 6.5

notafinal = (n1+n2+n2)/3
print(f"### Notas do Aluno ###")
print(f"Nota-1: {n1}, Nota-2: {n2}, Nota-3: {n3}")
print(f"A média final do aluno:{notafinal:.2f}")