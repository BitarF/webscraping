from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
from datetime import date

# Abre o arquivo .csv e adiciona dos dados que serão obtidos.
arquivo = 'boa_dica.csv'
arq = open(arquivo, 'a')
# titulo = ('Data' + ';' + 'Modelo' + ';' + 'Preço' + '\n')
# arq.write(titulo)

# Lista de sites:
page_urls = ['https://www.boadica.com.br/pesquisa/cpu_proc/precos?ClasseProdutoX=5&CodCategoriaX=27&XT=13&XE=5&modelo=168636&regiao=A&em_box=&cl=&preco_min=&preco_max=',
             'https://www.boadica.com.br/pesquisa/cpu_plmae/precos?ClasseProdutoX=5&CodCategoriaX=13&XT=2&XE=2&XG=4&modelo=164686&regiao=A&em_box=&cl=&preco_min=&preco_max=',
             'https://www.boadica.com.br/pesquisa/cpu_proc/precos?ClasseProdutoX=5&CodCategoriaX=3&XG=15&modelo=165948&regiao=A&em_box=&cl=&preco_min=&preco_max=',
             'https://www.boadica.com.br/pesquisa/cpu_plmae/precos?ClasseProdutoX=5&CodCategoriaX=26&XG=15&modelo=158578&regiao=A&em_box=&cl=&preco_min=&preco_max=',
             'https://www.boadica.com.br/pesquisa/cpu_proc/precos?ClasseProdutoX=5&CodCategoriaX=3&XG=22&modelo=174944&regiao=A&em_box=&cl=&preco_min=&preco_max=',
             'https://www.boadica.com.br/pesquisa/cpu_plmae/precos?ClasseProdutoX=5&CodCategoriaX=26&XG=22&modelo=175127&regiao=&em_box=&cl=&preco_min=&preco_max=',
             'https://www.boadica.com.br/pesquisa/mem_cpu/precos?ClasseProdutoX=3&CodCategoriaX=14&XT=9&XK=10&modelo=144771&regiao=A&em_box=&cl=&preco_min=&preco_max=']

lista = []

# Data da busca
today = date.today()
data = today.strftime("%d/%m/%Y")

# Loop na lista de sites, abre no BeautyfulSoup e fecha o client
for page in page_urls:
    uClient = uReq(page)
    page_soup = Soup(uClient.read(), "html.parser")
    uClient.close()

    # Pegando o modelo
    containers = page_soup.findAll("div", {"class": "row preco detalhe"})
    contain = containers[0]
    modelo = contain.span.text.strip()

    # Pegando o preço
    containers = page_soup.findAll("div", {"class": "col-md-1 preco"})
    contain = containers[0]
    preco = contain.text.strip()

    # Printa no console e escreve no banco de dados
    print('modelo: '+ modelo, '     Preço: ' + preco)
    arq.write(data + ';' + modelo + ';' + preco + '\n')

# Fechar e termina de suar o arquivo .csv
arq.close()