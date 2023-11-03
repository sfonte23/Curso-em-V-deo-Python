from time import sleep
n = int(input("Digite um número: "))
c=0
for time in range(0,5):
    print(".")
    sleep(0.5)
for i in range(1,n+1):
    if n%i == 0:
        print(f'\033[32m{i}\033[m, ',end='')
        c+=1
    else:
        print(f'\033[31m{i}\033[m, ',end='')
if c == 2:
    print(f"você escolheu o número {n} e ele foi divisível  {c} vezes")
    print(f"Por essa razão ele é \033[31mPRIMO\033[m")
else:
    print(f"Você escolheu {n} e ele é divisível por {c} números")
    print(f"Por essa razão ele \033[31mNÃO É PRIMO\033[m")