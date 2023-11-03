'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''

from random import randint

print('=-'*15)
print('    VAMO JOGAR PAR OU ÍMPAR')
print('=-'*15)

n1 = randint(1,10)
c=0
while True:
    n2 = int(input('\nDigite um Valor: '))
    p_i = ' '
    while p_i not in 'PI':
        p_i = input('Par ou Ímpar [P/I]? ').upper().strip()[0]
    n3 = 'Par' if (n1+n2)%2 == 0 else 'Impar'
    if n3.upper()[0] != p_i:
        resposta = "GAME OVER"
        print(f'''
          Você selecionou \033[31m{n2}\033[m 
          Computador selecionou \033[31m{n1}\033[m 
          A soma é {n1+n2} e deu {n3}.
          \033[031m{resposta}\033[m''')
        break
    else:
        resposta = "Acertou!"
        print(f'''
          Você selecionou \033[31m{n2}\033[m 
          Computador selecionou \033[31m{n1}\033[m 
          A soma é {n1+n2} e deu {n3}.
          \033[032m{resposta}\033[m''')
        c=+1  
    
print(f'\nVocê venceu {c} vez(es)')
