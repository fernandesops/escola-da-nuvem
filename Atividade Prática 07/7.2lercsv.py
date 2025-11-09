import csv

def ler_csv(nome_arquivo: str):

    try:

        with open(nome_arquivo, "r", encoding="utf-8") as f:
            

            reader = csv.DictReader(f)
            
            print(f"--- Lendo dados de '{nome_arquivo}' ---")
            

            for linha in reader:
                print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
                
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

ler_csv("pessoas.csv")