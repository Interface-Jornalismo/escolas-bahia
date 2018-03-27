#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup as BS 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

pagina_inicial = "http://escolas.educacao.ba.gov.br/escolas"

browser = webdriver.Chrome(chrome_options=options)
browser.get(pagina_inicial)
browser.save_screenshot('screenshot.png')

