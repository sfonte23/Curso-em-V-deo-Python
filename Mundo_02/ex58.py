from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar?''',end = '\n\n')
n = randint(0,10)
p = False
c=0

while p != n:
    p = int(input('Qual é o seu palpite? '))
    c += 1
    if p > n:
        print('Menos... Tente mais uma vez.\n')
    if p < n:
        print('Mais... Tente outra vez.\n')

print(f'\033[32mACERTOU!!!\033[m Você precisou de {c} tentativas.',end='')
if c >= 5:
    print('Poderia ter sido melhor!')
else:
    print('Parabéns, foi rápido!')