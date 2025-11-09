def calcular_preco_final():
    try:
        preco_original = float(input("Digite o preço original do produto: R$ "))
        percentual_desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))

        if preco_original < 0 or percentual_desconto < 0:
            print("Erro: Os valores não podem ser negativos.")
            return

        valor_desconto = preco_original * (percentual_desconto / 100)
        preco_final = preco_original - valor_desconto

        print("\n--- Recibo ---")
        print(f"Preço Original: R$ {preco_original:.2f}")
        print(f"Desconto de {percentual_desconto}%: R$ {valor_desconto:.2f}")
        print(f"Preço Final: R$ {preco_final:.2f}")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")


calcular_preco_final()