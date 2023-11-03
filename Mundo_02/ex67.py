'''Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário
O programa será interrompido quando o número solicitado for negativo'''
c=0
while True:
    print('-'*25)
    n = int(input('''Digite um número para ver a tabuada, 
para sair digite um número negativo: '''))
    print('-'*25)
    if n < 0:
        break
    while c <= 11:
        print(f'{n} x {c:2} = {n*c:2}')
        c+=1
        if c == 11:
            c=0
            break
print('\nObrigado!')