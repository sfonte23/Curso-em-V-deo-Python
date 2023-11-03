'''Crie um programa onde 4 jogadores joguem um dado e 
tenham resultados aleatórios. Guarde esses resultados 
em um dicionário em Python. 
No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

jogadas = dict()
print('Valores Sorteados:')
for i,j in enumerate(range(1,5)):
    jogadas[f'Jogador {i+1}'] = (randint(1,6))
    print(f'O Jogador {i+1} tirou {jogadas[f"Jogador {i+1}"]} no dado.')
    sleep(0.5)
print('-='*20)
print(f'{"====== RANKING DOS JOGADORES ======":^40}')
ranking = dict()
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse = True)
for k,v in enumerate(ranking):
    print(f'     {k+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
