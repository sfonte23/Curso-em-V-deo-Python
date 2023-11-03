'''Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador 
e quantos gols ele marcou. O programa deverá ser capaz 
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='',gols=0):
    """
    A função recebe a informação da ficha e retorna a informação
    :Parâm nome: Nome do Jogador
    :Parâm gols: Quantidade de Gols marcados
    :return: Informação do Jogador
    """
    if nome == '':
        nome = '<desconhecido>'
    
    
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'

#Programa Principal
print('-'*20)
n = input('Nome do Jogador: ')
g = str(input('Número de Gols: '))
if g.isnumeric():
    g= int(g)
else:
    g = 0
print(ficha(n,g))