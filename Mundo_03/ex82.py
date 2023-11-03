'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em 
uma lista. Depois disso, crie duas listas extras que vão conter 
apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''

lista =[]
listapar = []
listaimpar = []

while True:
    numero = int(input(f"Digite um valor: "))
    lista.append(numero)
    if numero %2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)

    n = input('Quer continuar [S|N]? ')[0]
    if n in 'Nn':
        break

print('=-'*20)
print(f'Você digitou {len(lista)} elemento(s).')
print(f'Sua lista completa é {sorted(lista)}')
print(f'Sua lista par é {sorted(listapar)}')
print(f'Sua lista ímpar é {sorted(listaimpar)}')