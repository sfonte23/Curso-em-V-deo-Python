'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e 
tambem indique o menor e o maior valor que estão na tupla.'''

from random import randint
numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f'Os números sorteados foram: {numeros}')
print(f'O maior número foi: {sorted(numeros)[-1]}')
print(f'O menor número foi: {sorted(numeros)[0]}')
print('=-'*15+'\nMétodo 2')
print(f'O maior número foi: {max(numeros)}')
print(f'O menor número foi: {min(numeros)}')