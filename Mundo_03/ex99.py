'''Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar 
todos os valores e dizer qual deles é o maior.'''

def maior(*n):
    print('=-'*15)
    maior = 0
    print(f'Foram informados {len(n)} valores ao todo: ',end='')
    for j,i in enumerate(n):
        if j == 0:
            maior = i
            print(i,end=' ')
        else:
            if i > maior:
                maior = i
                print(i,end=' ')
            else:
                print(i,end=' ')
    print(f'\nO maior informado foi {maior}')

#programa Principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()