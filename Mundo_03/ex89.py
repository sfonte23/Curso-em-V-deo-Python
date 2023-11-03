'''Crie um programa que leia nome e duas notas de vários alunos e 
guarde tudo em uma lista composta. No final, mostre um boletim contendo 
a média de cada um e permita que o usuário possa mostrar 
as notas de cada aluno individualmente.'''
alunos = []
while True:
    nome = str(input('Nome: ')).title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    alunos.append([nome,n1,n2])
    print('=-'*15)
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    print('=-'*15)
    if 'N' in continuar:
        break
print(f'\nNº|{"Nome":^15}| MÉDIA')
print('-'*25)
for n,nome in enumerate(alunos):
    print(f'{n} |{nome[0]:^15}| {((nome[1]+nome[2])/2):^6.1f}')
print('-'*25)

while True:
    consulta = int(input('Qual aluno deseja saber as notas? \033[31m[999 para sair]\033[m '))
    if consulta == 999:
        print('\033[32m-> Saindo <-\033[m')
        break
    elif consulta > len(alunos)-1:
        print(f'\033[31mOpção Inválida\033[m')
    else:
        print(f'Notas de {alunos[consulta][0]} foram: {alunos[consulta][1]} e {alunos[consulta][2]}')
        print('-'*25)