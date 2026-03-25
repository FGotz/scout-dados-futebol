import requests

url = "https://v3.football.api-sports.io/players"
minha_chave = "FOOTBALL_API_KEY" # Sua chave oficial

# Buscando o elenco do Corinthians (131) de 2023
querystring = {"team":"131","season":"2023"}
headers = {"x-apisports-key": minha_chave}

print("Coletando estatísticas do elenco...")
response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    dados = response.json()
    lista_jogadores = dados['response'] # Aqui está a lista com todos os atletas

    print(f"{'JOGADOR':<25} | {'GOLS':<5} | {'ASSIST':<6} | {'PASSES %'}")
    print("-" * 60)

    for item in lista_jogadores:
        nome = item['player']['name']
        
        # As estatísticas ficam dentro de uma lista chamada 'statistics'
        stats = item['statistics'][0] 
        
        gols = stats['goals']['total'] or 0
        assistencias = stats['goals']['assists'] or 0
        
        # Cálculo de precisão de passe (se houver dados)
        passes_totais = stats['passes']['total'] or 0
        passes_certos = stats['passes']['accuracy'] or 0
        
        print(f"{nome:<25} | {gols:<5} | {assistencias:<6} | {passes_certos}%")

else:
    print("Erro na consulta.")