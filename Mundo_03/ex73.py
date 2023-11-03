'''Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

bigBR2021 = (
    "Palmeiras", "Atlético Mineiro", "Fortaleza", "Bragantino", "Flamengo",
    "Athletico Paranaense", "Atlético Goianiense", "Fluminense", "Ceará", "Santos",
    "Bahia", "Internacional", "Juventude", "Corinthians", "América Mineiro",
    "Sport Recife", "São Paulo", "Grêmio", "Chapecoense", "Cuiabá"
)
p=1
print(f'A) Os 5 primeiros foram:\n')
for time in bigBR2021[0:5]:
    print(f'{p}º - {time}')
    p+=1
print('=-'*10+'\n')
u= 17
print (f'B) Os 4 últimos foram:\n')
for time in bigBR2021[-4:]:
    print(f'{u}º - {time}')
    u+=1
print('=-'*10+'\n')
print(f'C)Em ordem alfabética os times ficam:\n')
for time in sorted(bigBR2021[0:]):
    print(time)
print('=-'*10+'\n')
time = input('Qual time quer saber a posição? ')
print(f'A posição da Chapecoense é {bigBR2021.index(time)+1}º')
print('=-'*10+'\n')