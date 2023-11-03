s = 0
for i in range(1,501):
    if i %2 != 0:
        if i %3 == 0:
            s += i
print(f'A soma de todos os valores solicitadoes é {s}')


'''Outra forma:
soma = 0
for i in range(1,501,2):
    if i %3 == 0:
        soma = soma + i
print(f'A soma de todos os valores solicitadoes é {soma}')'''
