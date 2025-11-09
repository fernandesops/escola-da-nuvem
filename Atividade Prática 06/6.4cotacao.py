import requests

def consultar_cotacao():

    moeda_codigo = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()
    
    if not moeda_codigo:
        print("Código inválido.")
        return


    par_moedas = f"{moeda_codigo}-BRL"
    url = f"https://economia.awesomeapi.com.br/json/last/{par_moedas}"
    
    try:

        response = requests.get(url)
        response.raise_for_status() 
        
        dados = response.json()
        
        chave_api = par_moedas.replace("-", "")
        
        if chave_api not in dados:
            print(f"Não foi possível encontrar a cotação para o par {par_moedas}.")
            return
            
        cotacao = dados[chave_api]

        print(f"\n--- Cotação: {cotacao.get('name', 'N/A')} ---")
        print(f"Valor Atual (Bid): R$ {float(cotacao.get('bid', 0)):.4f}")
        print(f"Máxima (High):     R$ {float(cotacao.get('high', 0)):.4f}")
        print(f"Mínima (Low):      R$ {float(cotacao.get('low', 0)):.4f}")
        print(f"Última Atualização: {cotacao.get('create_date', 'N/A')}")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Erro: O par de moedas '{par_moedas}' não foi encontrado.")
        else:
            print(f"Erro HTTP: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    except (KeyError, TypeError):
        print("Erro ao processar a resposta da API. A estrutura pode ter mudado.")


consultar_cotacao()