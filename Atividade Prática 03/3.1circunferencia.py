#A fórmula para calcular a área de uma circunferência é: área = π ×raio2. Considerando para este problema que π = 3.14159265: 
#Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
#Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
#Saída: Apresente a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal.


pi = 3.14159265

raio = float(input("Digite o raio: "))

circunferencia = pi * (raio**2)

print(f"área = {circunferencia:.4f}")