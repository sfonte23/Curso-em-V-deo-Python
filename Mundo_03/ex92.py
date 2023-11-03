'''Crie um programa que leia nome, ano de nascimento e 
carteira de trabalho e cadastre-o (com idade) em um 
dicionário. Se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e 
o salário. Calcule e acrescente, além da idade, 
com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
aposentadoria = {}
aposentadoria['Nome'] = str(input('Nome: '))
aposentadoria['Idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
aposentadoria['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if aposentadoria['CTPS'] != 0:
    aposentadoria['Contratação'] = int(input('Ano de Contratação: '))
    aposentadoria['Salário'] = f'R$ {float(input("Salário: "))}'
    aposentadoria['Aposentadoria'] = aposentadoria['Idade'] + ((aposentadoria['Contratação'] + 35) - datetime.now().year)
print('-='*15)
for k,v in aposentadoria.items():
    if k != 'Aposentadoria':
        print(f'-> {k} = {v}')
    else:
        print(f'-> {k} será com {v} anos')