import requests

CHAVE_API = "6182e9c5828e574fd73b898fa70539c5"
URL_BASE = "https://api.themoviedb.org/3/"

def obter_recomendacoes(id_filme):
    url = f"{URL_BASE}movie/{id_filme}/recommendations"
    parametros = {"api_key": CHAVE_API}
    resposta = requests.get(url, params=parametros)

    if resposta.status_code == 200:
        recomendacoes = resposta.json().get("results", [])
        # Formatar resultados de forma mais clara
        filmes_recomendados = [
            {
                "titulo": filme["title"],
                "data_lancamento": filme.get("release_date", "Não disponível"),
                "media_votos": filme.get("vote_average", "Não disponível")
            }
            for filme in recomendacoes[:5]
        ]
        return filmes_recomendados
    else:
        print(f"Erro ao buscar recomendações para o filme {id_filme} (status {resposta.status_code})")
        return []

# Exemplo de uso
if __name__ == "__main__":
    id_filme = 550  # ID de exemplo: Clube da Luta
    filmes_recomendados = obter_recomendacoes(id_filme)
    
    print("\nRecomendações de filmes:")
    for idx, filme in enumerate(filmes_recomendados, start=1):
        print(f"{idx}. {filme['titulo']} (Lançamento: {filme['data_lancamento']}, Nota: {filme['media_votos']})")