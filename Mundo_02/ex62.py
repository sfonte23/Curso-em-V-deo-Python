print("="*15)
print(" GERADOR DE PA")
print("="*15)

i=int(input('Escreva o primeiro termo: '))
r=int(input('Escreva a razão de sua PA: '))
termo = i
c = 0
total = 0
n = 10

while n != 0:
    total += n
    while c < total:
        print(F'{termo} -> ',end='')
        termo+=r
        c+=1
    print('PAUSA')
    n= int(input("Quantos termos você quer mostrar a mais? "))

print(f'Você teve {c} termos')
