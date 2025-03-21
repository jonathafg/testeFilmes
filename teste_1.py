import requests
import json
from collections import Counter

CHAVE_API = "6182e9c5828e574fd73b898fa70539c5"
URL_BASE = "https://api.themoviedb.org/3/"

def obter_detalhes_filme(id_filme):
    url = f"{URL_BASE}movie/{id_filme}"
    parametros = {"api_key": CHAVE_API}
    resposta = requests.get(url, params=parametros)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

def obter_elenco_filme(id_filme):
    url = f"{URL_BASE}movie/{id_filme}/credits"
    parametros = {"api_key": CHAVE_API}
    resposta = requests.get(url, params=parametros)
    if resposta.status_code == 200:
        return resposta.json().get("cast", [])
    else:
        return []

def analisar_filmes(ids_filmes):
    contagem_atores = Counter()
    contagem_generos = Counter()
    receita_atores = Counter()

    for id_filme in ids_filmes:
        dados_filme = obter_detalhes_filme(id_filme)
        if not dados_filme:
            continue

        # Contar gêneros
        for genero in dados_filme.get("genres", []):
            contagem_generos[genero["name"]] += 1

        # Contar atores e bilheteira
        elenco = obter_elenco_filme(id_filme)
        for membro_elenco in elenco:
            nome_ator = membro_elenco.get("name", "Desconhecido")
            contagem_atores[nome_ator] += 1
            receita_atores[nome_ator] += dados_filme.get("revenue", 0)

    # Top 5 atores por bilheteira
    top_atores = receita_atores.most_common(5)

    # Salvar resultados em JSON
    resultados = {
        "participacao_por_ator": dict(contagem_atores),
        "frequencia_generos": dict(contagem_generos),
        "top_atores_bilheteria": top_atores
    }

    with open("resultados_analise.json", "w") as arquivo_json:
        json.dump(resultados, arquivo_json, indent=4)

    print("Análise concluída! Resultados salvos em 'resultados_analise.json'.")

# Exemplo de uso
if __name__ == "__main__":
    ids_filmes = [550, 299536, 597]  # IDs de exemplo
    analisar_filmes(ids_filmes)