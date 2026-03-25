import pandas as pd
from google import genai # <-- Importando a biblioteca nova!

# 1. Configurando a IA com a nova sintaxe
minha_chave_ia = "GEMINI_API_KEY" # Cole sua chave que começa com AIzaSy...
cliente = genai.Client(api_key=minha_chave_ia)

# 2. Lendo os dados que salvamos na Semana 2
print("1. Lendo a base de dados do Pandas...")
df = pd.read_csv("relatorio_corinthians.csv")

# Filtrando jovens e transformando em texto
jovens = df[df['Idade'] < 24]
dados_em_texto = jovens.to_string(index=False) 

# 3. Criando o Prompt (O Comando para o Olheiro Virtual)
prompt = f"""
Atue como um olheiro-chefe de futebol altamente analítico, especialista em revelar talentos para o Corinthians.
Aqui estão os dados estatísticos das nossas jovens promessas (menos de 24 anos) referentes à temporada analisada:

{dados_em_texto}

Com base EXCLUSIVAMENTE nestes números, escreva um relatório de scouting profissional respondendo:
1. Análise de Destaques: Quem parece ser o jogador mais promissor (ou que mais participou) e por quê?
2. Alerta de Fundamentos: Existe algum jogador que precisa de treinos urgentes de passe?
3. Resumo Executivo: Qual o potencial geral dessa garotada com base nesses dados limitados?
"""

# 4. Enviando para o Gemini (Sintaxe atualizada e modelo mais novo)
print("2. Enviando dados para o Olheiro Virtual... Aguarde a análise.")
resposta = cliente.models.generate_content(
    model='gemini-2.5-flash', # Usando o modelo super rápido mais recente
    contents=prompt
)

# 5. Salvando o resultado em um arquivo de texto
with open("relatorio_scout_ia.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(resposta.text)

print("\n✅ Relatório gerado com sucesso! Abra o arquivo 'relatorio_scout_ia.txt' para ler a análise.")