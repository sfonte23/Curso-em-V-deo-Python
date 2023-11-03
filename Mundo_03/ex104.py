'''Crie um programa que tenha a função leiaInt(), 
que vai funcionar de forma semelhante 'a função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''
def leiaInt(txt):
    while txt != int:
        txt = str(input('Digite um número: '))
        if txt.isnumeric():
            return txt
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')

#Programa Principal
print('-'*30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')