#Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. Calcule o salário do funcionário e exiba o resultado formatado corretamente.
#Entrada:
#O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:
#Número do funcionário (numero_funcionario).
#Quantidade de horas trabalhadas (horas_trabalhadas).
#Valor recebido por hora (valor_por_hora).

numero_funcionario = int(input("Digite o Número do funcionário:"))

horas_trabalhada = int(input("Digite a Quantidade de horas trabalhadas:"))

valor_por_hora = float(input("Valor recebido por hora:"))

salario = horas_trabalhada * valor_por_hora

print(f"O Salário recebido = R$ {salario:.2f}")