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
    escolas = browser.find_elements_by_class_name('.views-row')

    escola_links = escolas.find_elements_by_tag_name('a')

for i in range(0, 71):
    get_escolas(browser, i)
    