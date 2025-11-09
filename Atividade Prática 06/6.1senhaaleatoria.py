import random
import string

def gerar_senha_aleatoria():

    try:

        tamanho = int(input("Digite o número de caracteres da senha: "))
        
        if tamanho <= 0:
            print("O tamanho deve ser um número positivo.")
            return

        caracteres = string.ascii_letters + string.digits + string.punctuation


        senha_lista = random.choices(caracteres, k=tamanho)
        

        senha_gerada = "".join(senha_lista)

        print("-" * 30)
        print(f"Senha Aleatória Gerada: {senha_gerada}")
        print("-" * 30)

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")

gerar_senha_aleatoria()