n = False
soma = 0
contador = 0

while n != 999:
    n = int(input("Digite um número \033[31m[999 para parar]: \033[m"))
    if n != 999:
        soma += n
        contador +=1
print(f"Você digitou {contador} números e a soma entre eles foi {soma}")