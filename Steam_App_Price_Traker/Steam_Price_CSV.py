import requests
import csv
from datetime import datetime

def converter_preco(texto_preco):
    limpo = texto_preco.replace("R$", "").replace(" ", "").replace(",", ".")
    try:
        return float(limpo)
    except ValueError:
        return float('inf')

def processar_busca(app_id):
    parametros = {"appids": app_id, "cc": "br"}
    url = "https://store.steampowered.com/api/appdetails"
    response = requests.get(url, params=parametros)
    response.raise_for_status()
    
    dados_do_jogo = response.json()[app_id]["data"]
    nome = dados_do_jogo["name"]
    preco_formatado = dados_do_jogo["price_overview"]["final_formatted"]
    preco_atual_numero = converter_preco(preco_formatado)

    # 2. Lê o histórico
    caminho_csv = "historico_precos.csv"
    menor_preco_historico = float('inf')
    melhor_preco_texto = "R$ ---"
    melhor_data_texto = "--/--/----"

    try:
        with open(caminho_csv, mode="r", encoding="utf-8") as arquivo_leitura:
            leitor = csv.reader(arquivo_leitura)
            for linha in leitor:
                if len(linha) > 0 and linha[0] == nome:
                    preco_linha_numero = converter_preco(linha[1])
                    if preco_linha_numero < menor_preco_historico:
                        menor_preco_historico = preco_linha_numero
                        melhor_preco_texto = linha[1]
                        melhor_data_texto = linha[2]
    except FileNotFoundError:
        pass 

    hoje = datetime.now()
    data_atual = hoje.strftime("%d/%m/%Y")
    hora_atual = hoje.strftime("%H:%M:%S")

    if preco_atual_numero < menor_preco_historico:
        with open(caminho_csv, mode="a", newline="", encoding="utf-8") as arquivo_escrita:
            escritor = csv.writer(arquivo_escrita)
            escritor.writerow([nome, preco_formatado, data_atual, hora_atual])
        
        melhor_preco_texto = preco_formatado
        melhor_data_texto = data_atual

    return melhor_preco_texto, melhor_data_texto, preco_formatado