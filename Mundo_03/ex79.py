'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos 
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''
lista = []
print('=-'*15)
while True:
    n = int(input('Digite um número para a lista: '))
    if n in lista:
        while True:
            continuar = input('\033[31mNúmero já na lista!\033[m Deseja continuar? [S/N]').upper()[0]
            if continuar in 'SN':
                break
        if continuar == 'N':
            break
    else:
        lista.append(n)
        while True:
            continuar = input('Número cadastrado, deseja continuar? [S/N] ').upper()[0]
            if continuar in 'SN':
                break
        if continuar == 'N':
            break
print('=-'*15)
print(f'Os números digitados foram: {sorted(lista)}')