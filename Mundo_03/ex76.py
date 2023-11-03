'''Exercício Python 076: Crie um programa que tenha uma tupla única 
com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, 
organizando-os dados em forma tabular.'''


itens_loja_praia = (
    "Protetor solar", "R$ 25.99",
    "Toalha de praia", "R$ 18.50",
    "Guarda-sol", "R$ 45.99",
    "Chapéu de praia", "R$ 12.75",
    "Biquíni", "R$ 39.99",
    "Shorts de praia", "R$ 29.99",
    "Óculos de sol", "R$ 20.99",
    "Chinelos", "R$ 15.25",
    "Cooler", "R$ 49.99",
    "Prancha de Surf", "R$ 149.99"
)
print('=-'*30)
print(f'{"LOJA PRAIANA DO SÉRGIO":^60}')
print('-='*30)

for i in range(0, len(itens_loja_praia), 2):
    item = itens_loja_praia[i].title()
    preco = itens_loja_praia[i + 1]
    print(f'{item:.<50} {preco:>7}')
print('-='*30)