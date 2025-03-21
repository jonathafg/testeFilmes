# testeFilmes

Este projeto contém dois scripts Python que utilizam a API do **The Movie Database (TMDb)** para análise e recomendação de filmes. Siga as instruções abaixo para configurar e executar os scripts.

## Pré-requisitos

Antes de rodar os scripts, você precisa:
1. **Python 3.8 ou superior** instalado no seu computador. Baixe em [python.org](https://www.python.org/).

## Estrutura do Projeto

```plaintext
.
├── teste_1.py              # Script para análise de dados de filmes
├── teste_2.py              # Script para recomendação de filmes
├── requirements.txt        # Lista de bibliotecas necessárias
└── README.md               # Arquivo explicativo (este aqui!)
```
## Configuração do Ambiente
1. Clone ou baixe este repositório no seu computador.
2. Abra o terminal na pasta do projeto.
3.Instale as dependências necessárias executando:
  pip install -r requirements.txt

## Como Executar os Scripts

### 1. teste_1.py - Análise de Dados de Filmes
Este script analisa uma lista de IDs de filmes e gera as seguintes informações:
* Participação por ator (quantos filmes cada ator participou).
* Frequência de gêneros (quantas vezes cada gênero aparece na lista de filmes).
* Top 5 atores com maior bilheteira somada.

Uso
  1. Abra o arquivo teste_1.py e edite a variável ids_filmes para incluir os IDs dos filmes que deseja analisar:
```plaintext
ids_filmes = [550, 299536, 597]  # IDs de exemplo
```
  2. Execute o script com:

```plaintext
python teste_1.py
```
  3. O resultado será salvo no arquivo resultados_analise.json.

### 2. teste_2.py - Sistema de Recomendação de Filmes
Este script recebe o ID de um filme e retorna 5 recomendações baseadas em critérios fornecidos pela API do TMDb.

Uso
  1. No arquivo teste_2.py, altere a variável id_filme para o ID do filme desejado:

```plaintext
id_filme = 550  # ID de exemplo: Clube da Luta
```
  3. Execute o script com:

```plaintext
python teste_2.py
```
  3. As recomendações serão exibidas diretamente no terminal.

## Possíveis Problemas
Erro 401 (Unauthorized): Verifique se a chave da API foi inserida corretamente nos scripts.

Módulo requests não encontrado: Certifique-se de que instalou todas as dependências com o comando:

```plaintext
pip install -r requirements.txt
```
