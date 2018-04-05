#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup as BS 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import re

options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=options)

def infos_escola(link_da_escola, browser):
    base = "http://escolas.educacao.ba.gov.br"
    browser.get(base+link_da_escola)
    pagina_escola = BS(browser.page_source, 'html5lib')

    #Infos da escola
    escola_dict = {}
    escola_infos = pagina_escola.find('div', class_='escola-node-infos-col1')
    escola_dict['nome_da_escola'] = pagina_escola.find('div', class_='escola-node-title').text
    escola_dict['bairro'] = escola_infos.find(text=re.compile('Bairro:')).parent.next_sibling
    escola_dict['codigo_sec'] = escola_infos.find(text=re.compile('Sec:')).parent.next_sibling    
    escola_dict['municipio'] = escola_infos.find(text=re.compile('Município:')).parent.next_sibling

    print(escola_dict)
    
    #Acessa iframe da escola
    pagina_escola_content = pagina_escola.find('div', class_='transparencia-novo').iframe['src']
    browser.get(pagina_escola_content)
    pagina_iframe = BS(browser.page_source, 'html5lib')
    
    #Acha todos os elementos com dinheiro
    tr = pagina_iframe.find_all(text=re.compile('R\$'))
    for i in tr:
        if i.parent.name != 'td':
            print(i.parent.parent)

def get_escolas(browser, i):
    page = "http://escolas.educacao.ba.gov.br/escolas?tipo=next&page={}".format(i)
    browser.get(page)

    source = BS(browser.page_source, 'html5lib')
    content = source.find('div', class_='views_view__Escolas')
    escolas = content.find_all('span', class_='field-content')
    for escola in escolas:
        if escola.a != None:
            link_da_escola = escola.a['href']
            infos_escola(link_da_escola, browser)
            exit()


# for i in range(0, 71):
    # links_escolas = get_escolas(browser, i) 
links_escolas = get_escolas(browser, 1) 