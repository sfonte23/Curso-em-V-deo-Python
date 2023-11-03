'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada 
está com os parênteses abertos e fechados na ordem correta.'''

pilha = []
expressao = input('Digite sua expressão: ')
for e in expressao:
    if e == '(':
        pilha.append(e)
    elif e == ')':
       if len(pilha) > 0:
           pilha.pop()
       else:
          pilha.append(')')
          break

if len(pilha) == 0:
    print(f'Sua expressão é válida')
else:
    print('Sua expressão é inválida')