import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://lista.mercadolivre.com.br/'
pesquisa = "Iphone XR"
pesCerta = pesquisa.replace(" ", "-")
book = openpyxl.Workbook()
book.create_sheet('Produtos')
produtos = book['Produtos']

page = requests.get(url+pesquisa)
soup = BeautifulSoup(page.text, 'html.parser')
for exc in soup.find_all(class_="ui-search-item__group__element shops__items-group-details ui-search-installments ui-search-color--LIGHT_GREEN"):
    exc.decompose()
for exc in soup.find_all(class_="price-tag ui-search-price__part ui-search-price__original-value shops__price-part price-tag__disabled"):
    exc.decompose()
for exc in soup.find_all(class_="ui-search-item__group__element shops__items-group-details ui-search-installments ui-search-color--BLACK"):
    exc.decompose()


# def buscNome ():
#     i = 0
#     arrNome = []
#     while i < 10:
#         arrNome.append(soup.find_all(class_='ui-search-item__title shops__item-title')[i].get_text())
        
#         i = i+1
#     return print(arrNome)

# def buscPreco ():
#     i = 0
#     arrPreco = []
#     while i < 10:
#         arrPreco.append(soup.find_all(class_='price-tag-text-sr-only')[i].get_text())

#         i = i+1
#     return print(arrPreco)

# def buscLink ():
#     i = 0
#     arrLink = []
#     while i < 10:
#         arrLink.append(soup.find_all(class_='ui-search-item__group__element shops__items-group-details ui-search-link')[i].get('href'))

#         i = i+1
#     return print(arrLink)

def buscComplete ():
    i = 0
    x = 0
    arrBusc = []
    arrBusc = []
    arrBusc = []
    
    while i < 10:
        arrBusc.append(soup.find_all(class_='ui-search-item__title shops__item-title')[i].get_text())
        arrBusc.append(soup.find_all(class_='price-tag-text-sr-only')[i].get_text())
        arrBusc.append(soup.find_all(class_='ui-search-item__group__element shops__items-group-details ui-search-link')[i].get('href'))
        arrBusc[1] = arrBusc[1].replace("reais con", ",")
        arrBusc[1] = arrBusc[1].replace("reais", "")
        arrBusc[1] = arrBusc[1].replace("centavos", "")
        arrBusc[1] = arrBusc[1].replace(" ", "")
        # print(arrBusc)
        produtos.append(arrBusc)
        arrBusc = []
        i = i+1
    return book.save('Prod.xlsx')
        
# print(soup.prettify)
# buscNome()
# buscPreco()
# buscLink()
buscComplete()