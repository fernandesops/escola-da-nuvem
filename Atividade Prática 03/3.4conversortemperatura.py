# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.


temperatura = float(input("Digite o valor da temperatura: "))
tipo = input("Digite o tipo da temperatura (C, F, K): ").strip().upper()
destino = input("Escolha para qual temperatura Converter (C, F, K): ").strip().upper()

valor_celsius = 0.0
resultado = 0.0

if tipo == 'C':
    valor_celsius = temperatura
elif tipo == 'F':
        # (F - 32) * 5/9
    valor_celsius = (temperatura - 32) * 5/9
elif tipo == 'K':
        # K - 273.15
    valor_celsius = temperatura - 273.15
else:
    print(f"Erro: o tipo de temperatura '{tipo}' não é válida. Use C, F ou K.")
    exit()


if destino == 'C':
    resultado = valor_celsius
elif destino == 'F':
    # (C * 9/5) + 32
    resultado = (valor_celsius * 9/5) + 32
elif destino == 'K':
    # C + 273.15
    resultado = valor_celsius + 273.15
else:
    print(f"Erro: Unidade de destino '{destino}' não é válida. Use C, F ou K.")
    exit()

print(f"\n{temperatura:.2f}°{tipo} é igual a {resultado:.2f}°{destino}")