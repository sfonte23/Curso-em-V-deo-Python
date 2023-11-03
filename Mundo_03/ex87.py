'''Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

lista = []
somapares = somaterceira = maiorsegundalinha = 0
for linha in range(0,3):
    for coluna in range(0,3):
        n = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        lista.append(n)
        if n %2 == 0:
            somapares += n
print('=-'*20)
for num,matriz in enumerate(lista):
    if num == 2 or num == 5 or num == 8:
        print(f'[{matriz:^5}]')
        somaterceira += matriz
    else:
        print(f'[{matriz:^5}]',end='')

print('=-'*20)    
print(f'A) A soma de todos os valores pares foi: \033[31m{somapares}\033[m')
print(f'A) A soma dos valores da terceira coluna foi: \033[31m{somaterceira}\033[m')
for valor in lista[3:6]:
    if valor > lista[3]:
        maiorsegundalinha = valor
print(f'O maior valor da segunda linha foi: \033[31m{maiorsegundalinha}\033[m')