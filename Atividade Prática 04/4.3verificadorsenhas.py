def verificar_forca_senha():

    print("--- Verificador de Senha Forte ---")
    print("Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos 1 número.")
    print("Digite 'sair' a qualquer momento para encerrar.\n")


    while True:
        senha = input("Digite sua senha: ")

        if senha.lower() == 'sair':
            print("\nEncerrando o programa.")
            break 


        comprimento_ok = False
        tem_numero = False


        if len(senha) >= 8:
            comprimento_ok = True

        for caractere in senha:
            # .isdigit() retorna True se o caractere for um dígito (0-9)
            if caractere.isdigit():
                tem_numero = True
                break 

        if comprimento_ok and tem_numero:
            print("\n[SUCESSO] Senha forte aceita!")
            break 
        else:

            print("\n[ERRO] Senha fraca. Tente novamente.")
            if not comprimento_ok:
                print("- Sua senha deve ter pelo menos 8 caracteres.")
            if not tem_numero:
                print("- Sua senha deve conter pelo menos um número.")
            print("-" * 20) # Linha divisória para clareza

# --- Inicia o programa ---
if __name__ == "__main__":
    verificar_forca_senha()