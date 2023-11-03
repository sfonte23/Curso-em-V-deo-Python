'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

lista = []

print('=-'*15)
for i in range(0,5):
    lista.append(int(input(f"Digite um número para a posição {i}: ")))
print('=-'*15)

print(f'Sua lista contém {len(lista)} elementos')
print(f'Os elementos são: {lista}')

print(f'O maior é {max(lista)} e está na posição: ',end='')
for pmaior, v in enumerate(lista):
    if v == max(lista):
        print(f'{pmaior}...',end='')

print(f'\nO menor é {min(lista)} e está na posição: ',end='')
for pmenor, v in enumerate(lista):
    if v == min(lista):
        print(f'{pmenor}...')