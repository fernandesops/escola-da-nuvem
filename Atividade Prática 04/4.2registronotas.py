def calcular_media_turma():


    notas_validas = []
    
    print("--- Sistema de Registro de Notas da Turma ---")
    print("Digite as notas (de 0 a 10).")
    print("Para encerrar e calcular a média, digite 'fim'.\n")


    while True:

        entrada = input("Digite uma nota (ou 'fim'): ")

        #  .strip() para remover espaços (ex: " fim ")
        # .lower() para aceitar "fim", "Fim", "FIM", etc.
        if entrada.strip().lower() == 'fim':
            print("\nEncerrando a entrada de notas...")
            break  

        try:

            nota = float(entrada)


            if 0 <= nota <= 10:

                notas_validas.append(nota)
                print(f"-> Nota {nota} registrada com sucesso.")
            else:

                print(f"[AVISO] Nota inválida: {nota}. A nota deve estar entre 0 e 10.")
        
        except ValueError:

            print(f"[AVISO] Entrada inválida: '{entrada}'. Digite um NÚMERO ou 'fim'.")
        

    print("\n--- Resultado Final ---")
    

    if len(notas_validas) > 0:
        soma_das_notas = sum(notas_validas)
        quantidade_de_notas = len(notas_validas)
        media = soma_das_notas / quantidade_de_notas
        
        print(f"Total de notas válidas registradas: {quantidade_de_notas}")

        print(f"A média da turma é: {media:.2f}")
    else:

        print("Nenhuma nota válida foi registrada.")
        print("Não foi possível calcular a média.")


if __name__ == "__main__":
    calcular_media_turma()