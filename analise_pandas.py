import requests
import pandas as pd # Importando o nosso "Excel"

url = "https://v3.football.api-sports.io/players"
minha_chave = "FOOTBALL_API_KEY" # Sua chave oficial

querystring = {"team":"131","season":"2023"}
headers = {"x-apisports-key": minha_chave}

print("Baixando dados para o nosso DataFrame...")
response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    dados = response.json()
    lista_jogadores = dados['response']
    
    # 1. Criamos uma lista vazia para organizar as coisas
    dados_limpos = []

    # 2. Varremos o JSON bagunçado
    for item in lista_jogadores:
        nome = item['player']['name']
        idade = item['player']['age']
        
        stats = item['statistics'][0] 
        gols = stats['goals']['total'] or 0
        assistencias = stats['goals']['assists'] or 0
        passes_certos = stats['passes']['accuracy'] or 0
        
        # 3. Guardamos só o que importa no formato de "dicionário"
        dados_limpos.append({
            "Nome": nome,
            "Idade": idade,
            "Gols": gols,
            "Assistências": assistencias,
            "Passes Certos (%)": passes_certos
        })
        
    # 4. A MÁGICA DO PANDAS ACONTECE AQUI:
    df = pd.DataFrame(dados_limpos)
    
    print("\nTabela gerada com sucesso! Aqui estão os 10 primeiros:")
    print(df.head(10)) # O comando .head() mostra só o topo da tabela
    # -----------------------------------------
    # A HABILIDADE DE OURO: FILTROS DO PANDAS
    # -----------------------------------------
    
    # 1. Olheiro buscando jovens promessas (Idade menor que 24)
    jovens = df[df['Idade'] < 24]
    
    print("\n🔎 JOVENS PROMESSAS (Menos de 24 anos):")
    print(jovens[['Nome', 'Idade']]) # Mostrando só o Nome e a Idade
    
    # 2. Olheiro buscando quem participou de gols (Assistências maiores que 0)
    # E vamos organizar (sort) do maior para o menor
    garcons = df[df['Assistências'] > 0].sort_values(by='Assistências', ascending=False)
    
    print("\n🎯 OS GARÇONS DO TIME (Com assistências):")
    print(garcons[['Nome', 'Assistências']])

    # 3. Exportando para o Chefe (Salvando em Excel/CSV)
    df.to_csv("relatorio_corinthians.csv", index=False)
    print("\n✅ Tabela completa salva com sucesso no arquivo 'relatorio_corinthians.csv'!")
    
else:
    print("Erro na consulta.")


    