'''Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Diminuindo 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p,10))}')
print(f'Aumentando 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p,10))}')