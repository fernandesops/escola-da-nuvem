# Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D 
# segundo a fórmula: DIFERENCA = (A * B - C * D).
# Entrada: O arquivo de entrada contém 4 valores inteiros. 
# Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

a = int(input("Digite o valor A"))
b = int(input("Digite o valor B"))
c = int(input("Digite o valor C"))
d = int(input("Digite o valor D"))

diferenca = ((a * b) - (c * d))

print(f"DIFERENCA = {diferenca}")