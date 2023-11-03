'''Crie um código em Python que teste 
se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('O site em questão está acessível no momento.')
    print(site.read()) # pega o conteúdo html