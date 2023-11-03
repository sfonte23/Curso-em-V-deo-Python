'''Crie um programa que declare uma matriz de dimensão 3x3 
e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.'''
lista = []
for linha in range(0,3):
    for coluna in range(0,3):
        lista.append(int(input(f'Digite um valor para [{linha},{coluna}]: ')))

print('=-'*20)
for num,matriz in enumerate(lista):
    if num == 2 or num == 5:
        print(f'[{matriz:^5}]')
    else:
        print(f'[{matriz:^5}]',end='')