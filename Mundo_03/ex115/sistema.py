from lib.interface import *
from lib.arquivos import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = entrada(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do Sistema'])
    if resposta == 1 :
        print('-'*30)
        print(f'           Opção {resposta}')
        lerArquivo(arq)
    elif resposta == 2 :
        print('-'*30)
        print(f'           Opção {resposta}')
        print('-'*30)
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta  == 3:
        print('-'*30)
        print('      SAINDO... ATÉ LOGO!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
