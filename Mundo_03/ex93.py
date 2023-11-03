'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, 
incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
jogador['nome'] = input('Nome do Jogador: ')
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for n in range(1,p+1):
    gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {n}? ')))
jogador['gols'] = gols
jogador['total de gols'] = sum(gols)    
print('-='*20)
for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou um total de {len(jogador["gols"])} partidas.')
for i,v in enumerate(jogador['gols']):
    print(f'=> Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {sum(gols)} gols')