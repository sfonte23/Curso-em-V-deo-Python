def aumentar(preço=0,taxa=0,formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(preço=0,taxa=0,formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)

def dobro(preço=0,formato=False):
    res = preço*2
    return res if formato is False else moeda(res)

def metade(preço=0,formato=False):
    res = preço/2
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda ='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço = 0, aumento=0, diminuição=0):
    res = '-'*30
    res += f'\n{"RESUMO DO VALOR":^30}\n'
    res += f'-'*30
    res += f'\nPreço Analisado: \t{moeda(preço)}'
    res += f'\nDobro do Preço: \t{dobro(preço,True)}'
    res += f'\nMetade do preço: \t{metade(preço,True)}'
    res += f'\n{aumento}% de aumento: \t{aumentar(preço,aumento,True):>12}'
    res += f'\n{diminuição}% de aumento: \t{diminuir(preço,diminuição,True):>12}\n'
    res += f'-'*30
    return res