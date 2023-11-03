peso_maior = 0
peso_menor = 0
for p in range(1,6):
    peso = float(input(f"Peso da {p}ª pessoa: "))
    if p == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
           peso_maior = peso

        if peso < peso_menor:
            peso_menor = peso

print(f"\nO maior peso lido foi de {peso_maior}kg")
print(f"O menor peso lido foi de {peso_menor}kg\n")
