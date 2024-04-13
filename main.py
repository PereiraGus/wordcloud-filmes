import matplotlib.pyplot as plt
import requests as req
import pandas as pd
from dotenv import load_dotenv
import os
from wordcloud import WordCloud
import matplotlib.pyplot as pl
from datetime import datetime as dt
from pick import pick
from progressbar import progressbar
# openpyxl

load_dotenv()
sess = req.Session()
arquivo = None

print("""
==============================================================
========= Gerador de Wordcloud a partir de filmes ============
========================= PereiraGus +====== v0.1 ============
==============================================================
""")


def ler_arquivo():
    print("Escolha um arquivo para extrair seus filmes e suas avaliações:")
    arquivos = os.listdir("./planilhas")
    try:
        arquivo_escolhido, index = pick(arquivos, "Arquivos na pasta de planilhas:")
    except:
        print("Arquivos na pasta de planilhas: ", arquivos)
        arquivo_escolhido = input("Digite o nome completo do arquivo na pasta de planilhas: ")

    if arquivo_escolhido[-4:] != "xlsx":
        raise TypeError("Este arquivo não está no formato Excel \"xlsx\"")
    return pd.read_excel(f"./planilhas/{arquivo_escolhido}")


def criar_sessao():
    print("Se conectando ao The Movie Database...")
    apiKey = os.getenv("API_KEY")
    url = "https://api.themoviedb.org/3/authentication"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + apiKey
    }
    sess.headers.update(headers)
    authRes = sess.get(url, headers=headers)


def buscar_filme(titulo_filme: str) -> dict:
    searchUrl = f"https://api.themoviedb.org/3/search/movie?query={titulo_filme}&include_adult=true&language=pt-BR&page=1"
    searchRes = sess.get(searchUrl)
    return searchRes.json()


def formatar_filme(jsonf: dict) -> dict:
    filme_correspond = {"popularidade": 0}

    for filme in jsonf.get("results"):
        if "popularity" not in filme:
            filme.update({"popularity": 1})

        if filme.get("popularity") > filme_correspond.get("popularidade"):
            filme_correspond = {
                "id": filme.get("id"),
                "filme": filme.get("title"),
                "popularidade": filme.get("popularity")
            }
    return filme_correspond


def encontrar_palavras_chave(filme: dict) -> dict:
    categRes = sess.get(f"https://api.themoviedb.org/3/movie/{filme.get('id')}/keywords")
    jsonCategs = categRes.json()

    categorias = ""
    if categRes.status_code == 200:
        for categoria in jsonCategs.get("keywords"):
            categorias += f' {categoria.get("name")}'

    filme.update({"categorias": categorias})
    return filme


def gerar_wordcloud(categorias: str) -> WordCloud:
    print("Gerando o Wordcloud...")
    wc = WordCloud(background_color="white", repeat=False)
    wc.generate(categorias)
    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    plt.show()
    return wc


def balancear_pesos_notas() -> str:
    filmes_e_notas = ler_arquivo()
    filmes_encontrados = []
    resultados = ""

    print("Buscando e formatando filmes...")
    for i in progressbar(filmes_e_notas.index.to_list()):
        filme = formatar_filme(buscar_filme(filmes_e_notas["Filme"][i]))
        filme = encontrar_palavras_chave(filme)
        filmes_encontrados.append(filme.get("filme"))

        for i in range(0, filmes_e_notas["Probabilidade de assistir"][i]):
            resultados += f' {filme.get("categorias")}'

    print("Filmes encontrados:")
    print(filmes_encontrados)
    print("/!\\ Se algum filme foi indexado incorretamente, favor checar seu nome no"
          " The Movie Database como referência para atualizá-lo na planilha sendo lida.\n")
    return resultados


def salvar_wordcloud(wc: WordCloud):
    print("Gravando Wordcloud na pasta \"wordclouds\"...")
    try:
        svg_wc = wc.to_svg(embed_font=True)
        destino = os.getenv("DESTINO_GRAVACAO", "./wordclouds")
        data_hora = dt.now().strftime("%d-%m-%Y %H:%M")
        nome_arquivo = f'{destino}/wordcloud {data_hora}.svg'

        f = open(nome_arquivo, "w+")
        f.write(svg_wc)
        f.close()
        print("Sucesso!")
    except Exception as e:
        raise e

criar_sessao()
results = balancear_pesos_notas()
wc = gerar_wordcloud(results)
salvar_wordcloud(wc)
