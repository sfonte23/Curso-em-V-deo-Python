'''Aprimore o desafio 93 para que ele funcione 
com vários jogadores, incluindo um sistema de visualização 
de detalhes do aproveitamento de cada jogador.'''
jogador = {}
time = []
while True:
    jogador['nome'] = input('Nome do Jogador: ').title()
    p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for n in range(1,p+1):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {n}? ')))
    jogador['gols'] = gols
    jogador['total de gols'] = sum(gols)
    time.append(jogador.copy())
    jogador.clear()
    while True:
        continuar = input('Quer continuar? [S|N] ').upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if continuar == 'N':
        break
print('=-'*20)
print(f'{"COD":^4}|{"Nome":^20}|{"Gols":^15}|{"Total":>5}')
print('-'*40)
for i, j in enumerate(time):
    print(f'{i:^4}', end='')
    for d in j.values():
        print(f'{str(d):^15}', end='')
    print()
print('-'*40)

while True:
    proc = int(input('Qual jogador deseja ver os dados? \033[31m[999 para sair]\033[m '))
    if proc <= len(time)-1:
        print(f'==> LEVANTAMENTO DOS DADOS DE {time[proc]["nome"]}:'.upper())
        for i,j in enumerate(time[proc]['gols']):
            print(f'Na partida {i+1} fez {j} gols')
    elif proc == 999:
        print('tchau!')
        break
    else:
        print('ERRO! Código incorreto ou inexistente')