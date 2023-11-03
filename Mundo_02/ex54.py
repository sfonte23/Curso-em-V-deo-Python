from datetime import datetime

today = datetime.now()
maiores = 0
menores = 0

for p in range(1, 8):
    n = int(input(f"Em que ano a {p}ª pessoa nasceu? "))
    idade = today.year - n 
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Tivemos {maiores} maiores de idade e {menores} menores de idade')
