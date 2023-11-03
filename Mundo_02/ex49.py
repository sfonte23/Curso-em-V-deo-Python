n = int(input("Digite um número para ver sua tabuada: "))
print(f"A Tabuada de {n} é:")

for i in range(1,11):
    print(f"{n} x \033[31m{i}\033[m = {n*i}")
print("FIM!")