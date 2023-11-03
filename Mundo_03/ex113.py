'''Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaInt(txt):
        while True:
            try:
                n=int(input(txt))
            except (ValueError, TypeError):
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
                continue
            except (KeyboardInterrupt):
                 print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
                 return 0
            else:
                 return n
def leiaFloat(txt):
        while True:
            try:
                n=float(input(txt))
            except (ValueError, TypeError):
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
                continue
            except (KeyboardInterrupt):
                 print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
                 return 0
            else:
                 return n

#Programa Principal
print('-'*30)
i = leiaInt('Digite um número: ')
r = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')