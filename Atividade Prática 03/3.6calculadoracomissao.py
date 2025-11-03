# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
# efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
# sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 
# Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
# dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
# montante total das vendas efetuadas por este vendedor, respectivamente. 
# Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.


nome = (input("Digite seu Nome: "))
salario_fixo = float(input("Digite seu salário fixo: "))
total_de_vendas = float(input("Digite o total de vendas em R$: "))

comissao = 0.15
valor_comissao = total_de_vendas * comissao
total_a_receber = salario_fixo + valor_comissao

print(f"O funcionário {nome} deverá receber no TOTAL = R$ {total_a_receber:.2f}")



