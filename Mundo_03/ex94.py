'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoa = {}
pessoas = []
media = 0
while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M|F] ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        continuar = input('Quer continuar? [S|N] ').upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if continuar == 'N':
        break
print('=-'*20)
print(f'A) Foram cadastradas {len(pessoas)} pessoas')
print(f'B) A média de idade é {media/len(pessoas)}')
print(f'C) As mulheres da lista são: ',end='')
for m in pessoas:
    if m['sexo'] == 'F':
       print(m['nome'], end='...')
print(f'\nD) As pessoas com idade acima da média são: ',end='')
for i in pessoas:
    if i['idade'] > (media/len(pessoas)):
        print(f'{i["nome"]}', end='...')