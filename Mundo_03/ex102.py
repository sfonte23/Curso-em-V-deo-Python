'''Crie um programa que tenha uma função fatorial() 
que receba dois parâmetros: o primeiro que indique o número a calcular 
e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n=1,show=False):
    """ Essa função recebe 2 parâmetros e mostra ou nao o calculo fatorial.
    :parametro n = numero a ver o resultado do fatorial
    :parameto show = se desejar mostrar o cálculo
    """
    if n>0:
        if show:
            c=1
            resposta = f'{n}! = '
            while n > 0 :
                if n != 1:
                    resposta += f'{n} x ' 
                    c *= n
                    n -= 1
                else:
                    resposta += f'{n} ='
                    n -= 1
            resposta += f' \033[032m{c}\033[m'
            return resposta
        else:
            from math import factorial
            f = factorial(n)
            return f'O fatoral de {n} é \033[032m{f}\033[m'
    else:
        return f'\033[031mValor Inválido\033[m'

#Programa Principal
n = int(input('Digite um número para ver o seu fatorial: '))
show = 'Teste'
while show not in 'SN':
    show = input('Deseja ver o resultado? [S|N] ').upper()[0]
if show == 'S':
    show = True
else:
    show = False
print(fatorial(n,show))