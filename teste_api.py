import requests

# URL direta oficial da API-Football
url = "https://v3.football.api-sports.io/players"

# Cole a SUA NOVA CHAVE do site laranja aqui dentro das aspas
minha_chave_direta = "0409c56e2fc46d34f1bb200a330ae80c" 

# Vamos manter a busca no elenco do Corinthians (131) de 2023
querystring = {"team":"131","season":"2023"}

headers = {
	"x-apisports-key": minha_chave_direta
}

print("Consultando os dados do Timão direto na fonte...")
response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    dados = response.json()
    print("Sucesso! Dados recebidos.")
    # Pegando o nome do primeiro jogador da lista
    primeiro_jogador = dados['response'][0]['player']['name']
    print(f"Jogador encontrado: {primeiro_jogador}")
else:
    print(f"Erro na consulta: {response.status_code}")
    print("Motivo do erro:", response.text)