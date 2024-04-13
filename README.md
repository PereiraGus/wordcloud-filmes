# wordcloud-filmes
Script Python que gera uma nuvem de palavras baseada nos gostos cinematográficos do usuário.

![Versão 0.1](https://img.shields.io/badge/vers%C3%A3o-0.1-yellow
)

## Como utilizar?

### Requisitos
- Python 3
- Pip
- Excel (desktop ou online) ou qualquer outro programa capaz de gerar arquivos no formato ".xlsx"
- Uma conta no [The Movie Database](https://www.themoviedb.org/) (cadastro simples e gratuito)

### 1. Preparar arquivo
Crie um arquivo .xlsx (formato Excel 2007-365) com as colunas ```Filme``` e ```Propabilidade de Assistir```.

Na coluna de ```Filme```, informe o nome de um filme para incluir seus temas no Wordcloud. Caso necessite de referência, utilize o [The Movie Database](https://www.themoviedb.org/search?query=).

Na coluna ```Propabilidade de Assistir``` escolha um número de **0 à 5** determinando a probalidade de você assistí-lo ou, caso já o tenha feito, o quanto você gostou dele.

Para referência, utilize o arquivo ```gusHorrorExample.xlsx```, incluso na pasta ```/planilhas``` desse projeto.

### 2. Preparar o ambiente virtual (venv)
Iremos instalar as bibliotecas necessárias para o script em um ambiente virtual (venv), para evitar conflitos de versões e compatibilidade.

Para criá-lo, digite ```python -m venv venv``` na raíz do projeto.

Para entrar nele, utilizamos ```source venv/bin/activate```

A partir daqui, podemos instalar os pacotes necessários usando ```python -m pip install -r requirements.txt```

Após download e instalação dos pacotes, teremos todas as bibliotecas necessárias no nosso projeto.

**Quando desejar sair do programa**, use ```deactivate``` para sair do ambiente virtual. Para reentrar neste, utilize o comando "source ..." novamente.

*Obs:* É possível criar e acessar ambientes virtuais de outras maneiras, inclusive através de IDEs. Consulte a documentação da sua ferramenta escolhida para saber mais.

### 3 Definir chave do The Movies Database
Logue em sua conta do The Movie Database em seu [portal oficial](https://www.themoviedb.org/login?to=read_me&redirect=%2Freference%2Fintro%2Fauthentication) e copie sua chave de autenticação.

Copie o arquivo ```.env.template``` e nomeie essa cópia de ```.env```. Então, retire o comentário do parâmetro ```API_KEY``` e cole sua chave de api neste, conforme exemplo:
```API_KEY="XPTO..."```

O arquivo ```.env``` está inclúido no ```.gitignore```, ou seja, não será carregado no repositório Git, protegendo sua chave de API.

### 4. Executando
Com o terminal ou IDE dentro do ambiente virtual com os arquivos necessários, execute o arquivo ```main.py```.

