def classificador_par_impar():

    contagem_pares = 0
    contagem_impares = 0
    
    print("--- Classificador de Números (Par ou Ímpar) ---")
    print("Digite números inteiros (um por vez).")
    print("Para parar e ver o total, digite 'fim'.\n")


    while True:
        entrada = input("Digite um número inteiro (ou 'fim'): ")
        

        if entrada.strip().lower() == 'fim':
            print("\nEncerrando a entrada de dados...")
            break 

        try:

            numero = int(entrada)
            
            # 5. Lógica de Par ou Ímpar
            if numero % 2 == 0:
                print(f"-> {numero} é PAR.")
                contagem_pares += 1 # Incrementa o contador de pares
            else:
                print(f"-> {numero} é ÍMPAR.")
                contagem_impares += 1 # Incrementa o contador de ímpares
        
        except ValueError:

            print(f"[ERRO] '{entrada}' não é um número inteiro válido. Tente novamente.")
    
    print("\n--- Relatório Final ---")
    print(f"Quantidade de números PARES inseridos: {contagem_pares}")
    print(f"Quantidade de números ÍMPARES inseridos: {contagem_impares}")


# --- Inicia o programa ---
if __name__ == "__main__":
    classificador_par_impar()