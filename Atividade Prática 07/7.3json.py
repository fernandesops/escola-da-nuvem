import json

def escrever_json(nome_arquivo: str):

    pessoa = {
        "nome": "Raphael",
        "idade": 28,
        "cidade": "Fernandópolis",
        "habilidades": ["Python", "AWS", "SQL"]
    }
    
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(pessoa, f, indent=4, ensure_ascii=False)
            
        print(f"Arquivo '{nome_arquivo}' escrito com sucesso!")
        
    except IOError as e:
        print(f"Erro de E/S ao escrever o JSON: {e}")

def ler_json(nome_arquivo: str):

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            # json.load() carrega os dados do arquivo para um dicionário Python
            dados_lidos = json.load(f)
            
            print(f"\n--- Lendo dados de '{nome_arquivo}' ---")
            print(dados_lidos)
            
            print("\n--- Dados Formatados ---")
            print(f"Nome: {dados_lidos['nome']}")
            print(f"Idade: {dados_lidos['idade']}")
            print(f"Habilidade principal: {dados_lidos['habilidades'][0]}")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não é um JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


arquivo_json = "pessoa_dados.json"
escrever_json(arquivo_json)
ler_json(arquivo_json)