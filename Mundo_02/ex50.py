n=0
c=0 
for i in range(0,6):
    s = int(input(('Digite um número inteiro: ')))
    
    if s %2 == 0:
        if s == 0:
            c+=0
        else:
            c+=1
            n+= s
print(f'A soma dos {c} números pares informados é igual a {n}!')