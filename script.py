#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup as BS 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=options)

def get_escolas(browser, i):
    page = "http://escolas.educacao.ba.gov.br/escolas?tipo=next&page={}".format(i)
    browser.get(page)

    source = BS(browser.page_source, 'html5lib')
    content = source.find('div', class_='views_view__Escolas')
    escolas = content.find_all('span', class_='field-content')
    for escola in escolas:
        if escola.a != None:
            print(escola.a)
            print("")
    nome_da_escola = ''
    link_da_escola = ''
    
for i in range(0, 71):
    links_escolas = get_escolas(browser, i)
    