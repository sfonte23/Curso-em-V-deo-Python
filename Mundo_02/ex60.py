#calcule o fatorial
n = int(input('Digite um número para ver seu fatorial: '))
c=1
print(f'{n}! = ',end='')

if n>0:
    while n > 0 :
        if n != 1:
            print(f'{n} x ',end='') 
            c *= n
            n -= 1
            
        else:
            print(f'{n} =',end='') 
            n -= 1
    print(f' \033[032m{c}\033[m')
else:
    print('\033[031mValor Inválido\033[m')
'''from math import factorial
n = int(input('Digite um número para ver seu fatorial: '))
f = factorial(n)
print(f'O fatoral de {n} é {f}')'''