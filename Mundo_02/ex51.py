print("="*15)
print(" SUA PA AQUI")
print("="*15)

i=int(input('Escreva o primeiro termo: '))
r=int(input('Escreva a razão de sua PA: '))
decimo = i + (10-1) * r

for c in range(i,decimo+r,r):
    print(F'{c} -> ',end='')

print('FIM!')