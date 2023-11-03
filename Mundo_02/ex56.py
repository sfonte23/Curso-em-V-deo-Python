soma = 0 
contagem_idade = 0
hvelho = 0
contmulher = 0
nomehvelho = "Não definido"

for p in range (1,5):
    print(f"--- {p}ª PESSOA ----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))    
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    contagem_idade+=1
    soma += idade
    if p == 1 and sexo == "M":
        hvelho = idade
        nomehvelho = nome
    else:
        if hvelho < idade and sexo == "M":
            hvelho = idade
            nomehvelho = nome
        if sexo == "F" and idade <20:
            contmulher += 1

media = soma / contagem_idade
print(f"\nA média de idade do grupo é de {media} anos")
if nomehvelho == "Não definido":
    print(f"Não foi informado nenhum homem")
else:    
    print(f"O homem mais velho tem {hvelho} anos e seu nome é {nomehvelho}")

print(f"Ao todo são {contmulher} mulheres com menos de 20 anos")