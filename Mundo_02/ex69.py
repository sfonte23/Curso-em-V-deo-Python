'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadasrada 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A - Quantas pessoas tem mais de 18 anos?
B - Quantos homens foram cadastrados?
C - Quantas mulheres tem menos de 20 anos?'''

idade18 = homens = mulheres19 = 0

while True:
    print('~'*20) 
    print('\033[32mCADASTRE UMA PESSOA\033[m')
    print('~'*20)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'FM':
        sexo = input("Sexo [M|F]: ").upper().strip()[0]
    print('~'*20)

    if idade >= 18:
        idade18 += 1
    if sexo == 'M':
        homens += 1
    if sexo =='F' and idade < 20:
        mulheres19 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = input("\n\033[31mGostaria de continuar? [S|N] \033[m").upper().strip()[0]
    if resposta == 'N':
        print('Calculando...')
        break
        
print(f"O total de pessoas maior de 18 anos são de {idade18} pessoas")
print(f"Foram cadastrados {homens} homens")
print(f"Foram cadastradas {mulheres19} mulheres com menos de 20 anos.\n")
