'''Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra 'FIM', 
o programa se encerrará. Importante: use cores.'''
prog = False
while prog != 'FIM':
    print(f'\033[42;31m{"~"*50}\n {"Sistema Interativo PyHelp":^50}\n{"~"*50}\033[0;0m')
    prog = input('Função ou Biblioteca: ')
    print(f'\033[44m{"~"*50}\n "Acessando o manual do "{prog}"\n{"~"*50}\033[0;0m')
    print(f'\033[7m{help(prog)}\033[0;0m')
print(f'\033[41m{"~"*30}\n{"Até Logo!":^30}\n{"~"*30}\033[0;0m')