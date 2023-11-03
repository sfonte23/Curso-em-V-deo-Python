'''Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) 
e mostre a área do terreno.'''

def area(a,b):
    area = a*b
    print(f'A área de um terreno de {a} x {b} é de {area} m²')

print('  Controle de Terreno  ')
print('-----------------------')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)