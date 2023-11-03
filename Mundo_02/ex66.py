'''crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar 9999, que é a condição de parada (flag).
No final mostre quantos números foram digitados e qual foi a soma entre eles
Desconsidere a flag'''

contador = soma = 0
while True:
    n = int(input('Digite um número inteiro, \033[31mescolha 999 para parar:\033[m '))
    if n == 999:
        break
    soma+= n
    contador += 1
print(f'Você digitou {contador} números, a soma deles foi {soma}')