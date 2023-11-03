from time import sleep
#crie um menu
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
r = False

while r != 5:
    r= int(input('''\nO que deseja fazer?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa\n'''))

    if r == 1:
        print(f'A soma de {n1} + {n2} é igual a {n1+n2}')
    elif r == 2:
        print(f'A multiplicação de {n1} x {n2} é igual a {n1*n2}')
    elif r == 3:
        if n1>n2:
            print(f'O maior é o {n1}')
        elif n1==n2:
            print('Os números são iguais, não há maior.')
        else:
            print(f'O maior é o {n2}')
    elif r == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif r == 5:
        break
    else:
        print('\033[031mOpção inválida!\033[m')
    print(f'=-'*10)
    sleep(1)
print('Finalizando...')