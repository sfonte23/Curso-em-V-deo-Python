print("="*15)
print(" GERADOR DE PA")
print("="*15)

i=int(input('Escreva o primeiro termo: '))
r=int(input('Escreva a razão de sua PA: '))
d = i + (10-1) * r
c = 0
print(f'{i} -> ', end='')

while c < 9:
    print(F'{i+r} -> ',end='')
    i+=r
    c+=1

print('FIM!')