''' Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separados os valores 
pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

lista = [[],[]]

for i in range(1,8):
    valor = int(input(f'Digite o {i}º valor: '))
    if valor %2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print('=-'*20)
print(f'Os pares foram {sorted(lista[0])}')
print(f'Os ímpares foram {sorted(lista[1])}')