frase = input("Digite uma frase: ").upper().replace(" ","")
frase_invertida = frase[::-1]

print(f'A frase \033[31m{frase}\033[m invertida fica \033[32m{frase_invertida}\033[33m')
if frase == frase_invertida:
    print("É um Palíndromo")
else:
    print("Não é um Palindromo")

'''
Outra forma com FOR:

frase= str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso+= junto[letra]
if inverso == junto:
    print("É um Palíndromo")
else:
    print("Não é um Palindromo")'''
