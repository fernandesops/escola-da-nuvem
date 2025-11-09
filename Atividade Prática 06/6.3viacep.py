import requests

def consultar_cep():

    # 1. Pede o CEP e limpa (remove hifens e espaços)
    cep_input = input("Digite o CEP (apenas números): ").strip().replace("-", "")
    
    if not cep_input.isdigit() or len(cep_input) != 8:
        print("Erro: CEP inválido. Digite 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep_input}/json/"
    
    try:

        response = requests.get(url)
        response.raise_for_status()
        

        dados = response.json()
        

        if dados.get("erro"):
            print(f"CEP {cep_input} não encontrado.")
            return
            

        print("\n--- Endereço Encontrado ---")
        print(f"CEP: {dados.get('cep', 'N/A')}")
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados.get('bairro', 'N/A')}")
        print(f"Cidade: {dados.get('localidade', 'N/A')}")
        print(f"Estado: {dados.get('uf', 'N/A')}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API ViaCEP: {e}")


consultar_cep()