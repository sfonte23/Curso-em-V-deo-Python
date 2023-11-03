'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 
6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
print('-' * 30)
print(f"{'JOGUE NA MEGA SENA':^30}")
print('-' * 30)
jogos = int(input('Quanto jogos você quer que eu sorteie? '))
print(f'\n-=-=-= SORTEANDO {jogos} JOGOS =-=-=-')
jogo = []
for i,j in enumerate(range(0,jogos)):
    for n in range(0,6):
        numero = randint(1,60)
        while numero in jogo:
            numero = randint(1,60)
        jogo.append(numero)
    print(f'Jogo {i+1}: {sorted(jogo)}')
    sleep(0.5)
    jogo.clear()
    

print('-=-=-= BOA SORTE =-=-=-')
