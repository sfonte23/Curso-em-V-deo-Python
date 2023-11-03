'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista =[]

while True:
    lista.append(int(input(f"Digite um valor: ")))
    n = input('Quer continuar [S|N]? ').upper()[0]
    if n in 'Nn':
        break
  
print('=-'*10)
print(f'Você digitou {len(lista)} elemento(s).')
print(f'Os valores em ordem decrescente ficam: {sorted(lista, reverse=True)}')
if 5 in lista:
       print('O número 5 está na lista')
else:
     print('O número 5 não está na lista')
