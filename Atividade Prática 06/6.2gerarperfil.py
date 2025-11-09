import requests

def gerar_usuario_aleatorio():

    url = "https://randomuser.me/api/"
    
    try:

        response = requests.get(url)

        response.raise_for_status() 
    
        dados = response.json()

        usuario = dados["results"][0]
        
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("\n--- Perfil de Usuário Aleatório ---")
        print(f"Nome: {nome_completo}")
        print(f"Email: {email}")
        print(f"País: {pais}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API Random User: {e}")
    except KeyError:
        print("Erro: A estrutura da resposta da API mudou.")

gerar_usuario_aleatorio()