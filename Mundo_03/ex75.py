'''Exercício Python 075: Desenvolva um programa que leia quatro valores 
pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

numeros = (int(input('Digite o 1º número: ')),
           int(input('Digite o 2º número: ')),
           int(input('Digite o 3º número: ')),
           int(input('Digite o 4º número: '))
           )
print(f'\nVocê digitou: {numeros}')
print('-='*15+'\n')

print(f'A) O valor 9 aparece {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'B) O primeiro valor 3 aparece na {numeros.index(3)+1}ª posição')
else:
    print(f'B) O valor 3 não foi informado')
    
print(f'C) O números pares foram: ',end ='')

for p in numeros:
    if p %2 == 0 and p > 0:
         print(f'{p}, ',end='')