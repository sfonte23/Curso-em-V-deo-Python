'''FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, 
MAS SÓ ACEITE OS VALORES M OU F. 
CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO 
NOVAMENTE ATÉ TER UM VALOR CORRETO.'''

sexo =str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo != ('M') and sexo != ('F'):
    sexo = str(input('\033[31mDados Inválidos!\033[m Por favor, informe seu sexo: ')).strip().upper()[0]

print(f'Sexo \033[32m{sexo}\033[m registrado com sucesso, Obrigado!')