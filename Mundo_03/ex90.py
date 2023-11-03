'''Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

aluno = dict()

aluno['Nome'] = input('Nome do Aluno: ')
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
print('-='*20)
print(f' -> Nome igual a {aluno["Nome"]}')
print(f' -> Média igual a {aluno["Media"]}')
if aluno['Media'] >= 7:
    print(f' -> Situação é \033[32mAprovado\033[m ')
elif 5<= aluno['Media'] <7:
    print(f' -> Situação é \033[34mem Recuperação\033[m ')
else:
    print(f' -> Situação é \033[31mReprovado\033[m ')