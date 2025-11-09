import datetime

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    try:
        ano_atual = datetime.date.today().year

        if ano_nascimento > ano_atual:
            print("Erro: O ano de nascimento não pode ser no futuro.")
            return 0
        
        idade_em_anos = ano_atual - ano_nascimento
        
        idade_em_dias = idade_em_anos * 365
        
        return idade_em_dias

    except TypeError:
        print("Erro: O ano de nascimento deve ser um número inteiro.")
        return 0


ano = int(input("Digite o Ano de nascimento: "))

dias_de_vida = calcular_idade_em_dias(ano)
if dias_de_vida > 0:
    print(f"Uma pessoa que nasceu em {ano} tem aproximadamente {dias_de_vida} dias de vida.")