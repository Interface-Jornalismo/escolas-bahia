#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup as BS 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import re

options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=options)

def infos_escola(nome_da_escola, link_da_escola, browser):
    base = "http://escolas.educacao.ba.gov.br"
    browser.get(base+link_da_escola)
    pagina_escola = BS(browser.page_source, 'html5lib')
    pagina_escola_content = pagina_escola.find('div', class_='transparencia-novo').iframe['src']
    browser.get(pagina_escola_content)
    pagina_iframe = BS(browser.page_source, 'html5lib')

    campos = ["SALDO INICIAL TOTAL", "SALDO INICIAL PARA FUNCIONAMENTO DA UNIDADE ESCOLAR", "TOTAL DE RECURSOS RECEBIDOS PARA FUNCIONAMENTO DA UNIDADE ESCOLAR","TOTAL INVESTIDO PARA FUNCIONAMENTO DA UNIDADE ESCOLAR", "SALDO DISPONÍVEL PARA FUNCIONAMENTO DA UNIDADE ESCOLAR","SALDO INICIAL PARA ALIMENTAÇÃO ESCOLAR", "TOTAL DE RECURSOS RECEBIDOS PARA ALIMENTAÇÃO ESCOLAR", "TOTAL INVESTIDO PARA ALIMENTAÇÃO ESCOLAR", "SALDO DISPONÍVEL PARA ALIMENTAÇÃO ESCOLAR", "TOTAL DE RECURSOS RECEBIDOS NO ANO EM EXERCÍCIO", "TOTAL INVESTIDO PARA FUNCIONAMENTO DA UNIDADE ESCOLAR", "SALDO DISPONÍVEL PARA FUNCIONAMENTO DA UNIDADE ESCOLAR","SALDO INICIAL PARA ALIMENTAÇÃO ESCOLAR", "TOTAL DE RECURSOS RECEBIDOS PARA ALIMENTAÇÃO ESCOLAR", "TOTAL INVESTIDO PARA ALIMENTAÇÃO ESCOLAR", "SALDO DISPONÍVEL PARA ALIMENTAÇÃO ESCOLAR", "TOTAL DE RECURSOS RECEBIDOS NO ANO EM EXERCÍCIO", "RECEITA TOTAL NO ANO EM EXERCÍCIO", "INVESTIMENTO TOTAL NO ANO EM EXERCÍCIO", "SALDO DISPONÍVEL NO ANO EM EXERCÍCIO"]    

    
    tr = pagina_iframe.find_all(text=re.compile('R\$'))
    for i in tr:
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
            nome_da_escola = escola.a.text
            infos_escola(nome_da_escola, link_da_escola, browser)


# for i in range(0, 71):
    # links_escolas = get_escolas(browser, i) 
links_escolas = get_escolas(browser, 1) 