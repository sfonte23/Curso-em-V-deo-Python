numero = int(input("Digite um número: "))
soma = maior = menor = numero
contador = 1
continuar = input("Quer continuar? [S/N]: ").upper()

while continuar == "S":
    numero = int(input("Digite um número: "))
    contador+=1
    soma+=numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    continuar = input("Quer continuar? [S/N]: ").upper()

media = soma/contador
print(f'''\nVocê digitou {contador} números e a média foi {media}
O maior valor foi {maior} e o menor valor foi {menor}.''')