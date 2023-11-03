'''Crie um programa que tenha uma função chamada voto() 
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(ano):
    """Essa função recebe como parâmetro o ano de nascimento de uma pessoa,
    retornando um valor literal indicando se uma pessoa tem voto 
    NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""
    from datetime import date
    idade = date.today().year - ano1
    if idade < 16:
        return f'Você tem {idade} anos e não pode votar'
    elif 66 > idade > 17:
        return f'Você tem {idade} anos e é um eleitor obrigatório'
    else:
        return f'Você tem {idade} anos e é um eleitor facultativo'
#Programa Principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))