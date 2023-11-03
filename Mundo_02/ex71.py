'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
c50 = c20 = c10 = c1 = 0
print(f'='*30+'\n          BANCO UFPI\n'+'='*30+'\n')
valor = int(input("Qual valor deseja sacar? "))

if valor >= 50:
    c50 = valor//50
    valor = valor - (c50*50)
    print(f'Total de {c50} cédula(s) de R$50')
if valor >= 20:
    c20 = valor //20
    valor = valor - (c20*20)
    print(f'Total de {c20} cédula(s) de R$20')
if valor >= 10:
    c10 = valor //10
    valor = valor - (c10*10)
    print(f'Total de {c10} cédula(s) de R$10')
if valor >= 1:
    c1 = valor //1
    valor = valor - c1
    print(f'Total de {c1} cédula(s) de R$1')

print(f'='*30+'\nA UFPI Agradece! Volte Sempre.\n')