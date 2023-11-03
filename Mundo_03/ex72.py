'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso
se zero até vinte. Seu progrmaa deverá ler um número pelo teclado, entre 0 e 20 e mostrá-lo por extenso'''

n = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez",
    "Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")


while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if numero < 0 or numero >20:
            print('\033[31mVocê digitou um número inválido, tente novamente.\033[m\n'+'=-'*15)
        else:
            break
    print(f'Você digitou {n[numero]}')
    
    continuar = input('Deseja continuar? [S/N] ').upper().split()[0]
    if continuar == 'N':
        print('Obrigado!')
        break