''' 
rie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A- Qual o total gasto?
B- Quantos custam mais de 1000?
C- Qual é o nome do produto mais barato?
'''

total = caros = pbarato = pcaro = preco_caro = preco_barato = 0

print('-'*30)
print('     LOJA SUPER BARATÃO')
print('-'*30)

while True:
    produto = str(input('\nNome do Produto: ')).capitalize()
    valor = float(input('Preço: R$'))
    total += valor

    if valor > 1000:
        caros += 1
    
    if pcaro == 0 or pbarato ==0:
        pcaro = produto
        pbarato = produto
        preco_caro = valor
        preco_barato = valor
    
    if valor > preco_caro:
        preco_caro = valor
        pcaro = produto
    if valor < preco_barato:
        preco_barato = valor
        pbarato = produto
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('-'*30+'\nQuer Continuar [S|N]? ').upper().strip()[0]
    if continuar == 'N':
        print ('\n'+'~'*10+' SEU RECIBO '+'~'*10+'\n')
        break

print(f'O total de sua compra foi de R${total:.2f}')
print(f'Você comprou {caros} produtos acimas de R$1000!')
print(f'O produto mais barato foi {pbarato}')
print(f'O produto mais caro foi {pcaro}')