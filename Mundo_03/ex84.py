'''Faça um programa que leia nome e peso de várias pessoas, 
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

dadostotal = list()
pesomaior = pesomenor = 0
dados = list()
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(dadostotal) == 0:
        pesomaior = pesomenor = dados[1]
    else:
        if dados[1] > pesomaior:
            pesomaior = dados[1]
        elif dados[1] < pesomenor:
            pesomenor = dados[1]
        
    dadostotal.append(dados[:])
    dados.clear()
    continuar = input('Quer continuar? ').upper()[0]
    if continuar == 'N':
        break

print('=-'*15)
print(f'Ao todo você cadastrou {len(dadostotal)}')
print(f'O peso maior foi de {pesomaior} kg, referente a ',end='')
for p in dadostotal:
    if p[1] == pesomaior:
        print(f'{p[0]}... ',end='')
print(f'\nO peso menor foi de {pesomenor} kg, referente a ',end='')
for p in dadostotal:
    if p[1] == pesomenor:
        print(f'{p[0]}... ',end='')