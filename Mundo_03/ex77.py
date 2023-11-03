'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, 
para cada palavra, quais são as suas vogais.'''

palavras_padaria = (
    "Padeiro","Croissant","Bolo","Rosquinhas","Baguete",
    "Sonho","Torta","Pudim","Panetone","Biscoito"
)

for p in palavras_padaria:
    print(f'\nA palavra \033[32m{p}\033[m tem as vogais: ',end='')
    for letra in p.lower():
        if letra in 'aeiou':
            print(f'\033[31m{letra}\033[m ',end='')