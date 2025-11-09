import csv

def escrever_csv(nome_arquivo: str):

    colunas = ["Nome", "Idade", "Cidade"]
    
    # Dados a serem escritos
    dados = [
        {"Nome": "Lara", "Idade": 28, "Cidade": "Rio de Janeiro"},
        {"Nome": "Raphael", "Idade": 28, "Cidade": "Fernandópolis"},
        {"Nome": "Possari", "Idade": 29, "Cidade": "Osasco"},
        {"Nome": "Alan", "Idade": 25, "Cidade": "Minas Gerais"}
    ]
    
    try:

        with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
            

            writer = csv.DictWriter(f, fieldnames=colunas)
            

            writer.writeheader()
            

            writer.writerows(dados)
            
        print(f"Arquivo '{nome_arquivo}' escrito com sucesso!")
        
    except IOError as e:
        print(f"Erro de E/S ao escrever o arquivo: {e}")


escrever_csv("pessoas.csv")