'''Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade(). 
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'Diminuindo 10% de {p} é R${moeda.diminuir(p,10):.2f}')
print(f'Aumentando 10% de {p} é R${moeda.aumentar(p,10):.2f}')