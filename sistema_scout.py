import os
import requests
import pandas as pd
from google import genai
from dotenv import load_dotenv

class ScoutCorinthians:
    # 1. O Método Construtor (A recepção da nossa fábrica)
    # Ele recebe as chaves e prepara o ambiente assim que a classe é chamada
    def __init__(self, api_football_key, gemini_key):
        self.api_football_key = api_football_key
        self.gemini_client = genai.Client(api_key=gemini_key)
        self.url_base = "https://v3.football.api-sports.io/players"

    # 2. Operário 1: Especialista em buscar dados
    def buscar_dados_api(self, team_id="131", season="2023"):
        print("Buscando dados na API...")
        headers = {"x-apisports-key": self.api_football_key}
        params = {"team": team_id, "season": season}
        
        response = requests.get(self.url_base, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()['response']
        else:
            print("Erro ao buscar dados na API.")
            return None

    # 3. Operário 2: Especialista em Pandas (Filtra e Limpa)
    def processar_dados_pandas(self, dados_brutos):
        print("Processando e limpando dados com Pandas...")
        dados_limpos = []
        
        for item in dados_brutos:
            stats = item['statistics'][0] 
            dados_limpos.append({
                "Nome": item['player']['name'],
                "Idade": item['player']['age'],
                "Gols": stats['goals']['total'] or 0,
                "Assistências": stats['goals']['assists'] or 0,
                "Passes Certos (%)": stats['passes']['accuracy'] or 0
            })
            
        df = pd.DataFrame(dados_limpos)
        # Retorna apenas jogadores com menos de 24 anos
        return df[df['Idade'] < 24]

    # 4. Operário 3: O Olheiro Virtual (Integração com Gemini)
    def gerar_relatorio_ia(self, df_jovens):
        print("Enviando para o Olheiro Virtual (Gemini)...")
        dados_em_texto = df_jovens.to_string(index=False)
        
        prompt = f"""
        Atue como um olheiro-chefe de futebol. Analise as jovens promessas (menos de 24 anos):
        {dados_em_texto}
        
        Considerando que muitos podem ter 0 estatísticas por falta de minutagem em campo, 
        faça um relatório executivo breve apontando essa limitação técnica aos diretores e, 
        se houver algum dado positivo, destaque-o.
        """
        
        resposta = self.gemini_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        
        with open("relatorio_final_oop.txt", "w", encoding="utf-8") as f:
            f.write(resposta.text)
            
        print("✅ Relatório final salvo com sucesso em 'relatorio_final_oop.txt'!")

# ==========================================
# EXECUTANDO O SISTEMA (A Mágica Acontece Aqui)
# ==========================================
if __name__ == "__main__":
    # COLOQUE O LOAD_DOTENV AQUI DENTRO
    load_dotenv(override=True)
    
    CHAVE_FOOTBALL = os.getenv("FOOTBALL_API_KEY") 
    CHAVE_GEMINI = os.getenv("GEMINI_API_KEY")
    
    if not CHAVE_FOOTBALL or not CHAVE_GEMINI:
        print("❌ Erro de leitura no .env!")
        # Plano B: Se o .env falhar de novo, vamos colocar a chave direto aqui
        # apenas para você conseguir rodar o scout agora:
        CHAVE_FOOTBALL = "0409c56e2fc46d34f1bb200a330ae80c"
        CHAVE_GEMINI = "AIzaSyCsPap_6c4E_va2JZmQB_itojtfR_utjFo"
        print("⚠️ Usando chaves de contingência (Hardcoded).")

    # Ligamos a fábrica
    meu_sistema = ScoutCorinthians(CHAVE_FOOTBALL, CHAVE_GEMINI)
    
    # Iniciamos o trabalho
    dados_brutos = meu_sistema.buscar_dados_api()
    
    if dados_brutos:
        df_jovens = meu_sistema.processar_dados_pandas(dados_brutos)
        meu_sistema.gerar_relatorio_ia(df_jovens)