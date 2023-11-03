'''Faça um programa que tenha uma lista chamada números e 
duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma 
entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep

def sorteia(n):
    numeros = []
    for i in range(1,n+1):
        numeros.append(randint(1,10))
    print(f'Sorteando {n} valores: ',end='')
    for n in numeros:
        print(f'{n} ', end='',flush=True)
        sleep(0.5)
    print('PRONTO!')
    somaPar(numeros)

def somaPar(lst):
    print('=-'*20)
    soma = 0
    for n in lst:
        if n %2 == 0:
            soma += n
    print(f'Somando os valores pares de {lst}, temos: {soma}.')   
 
#Programa Principal
vezes = int(input('Quantos números deseja sortear? '))
sorteia(vezes)