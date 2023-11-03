from random import randint
from time import sleep
colors = {'VOCÊ':'\033[34m','fechador':'\033[m','PC':'\033[31m',"ciano":'\033[36m','GANHOU':'\033[32m'}
while True:
    print('\n'+"-=-" * 10)
    print(f'   PEDRA, TESOURA E PAPEL!')
    print("-=-" * 10)
    voce = int(input("Escolha um tipo:\n[1]🤜\n[2]✌\n[3]🖖\n[4]SAIR\n\nSua Opção: "))
    pc = randint(1,3)

    if voce != 4:
        print("Avaliando\n")
        sleep(1)
        print(".",end="")
        sleep(1)
        print(".",end="")
        sleep(1)
        print(".",end="")

    print("-=-" * 10+'\n')
    if pc == 1 and voce == 1:
        print("(\033[31mBot\033[m)🤜 \033[36m x\033[m 🤜 (\033[VOCÊ)\033[m")
        print("EMPATE")
    elif pc == 1 and voce == 2:
        print(f"({colors['PC']}PC{colors['fechador']})🤜 {colors['ciano']} x{colors['fechador']} ✌ ({colors['VOCÊ']}VOCÊ{colors['fechador']})")
        print(f"{colors['PC']}VOCÊ PERDEU{colors['fechador']}")
    elif pc == 1 and voce == 3:
        print(f"({colors['PC']}PC{colors['fechador']})🤜 {colors['ciano']} x{colors['fechador']} 🖖 ({colors['VOCÊ']}VOCÊ{colors['fechador']})")
        print(f"{colors['GANHOU']}VOCÊ GANHOU{colors['fechador']}")
    elif pc == 2 and voce == 1:
        print(f"({colors['PC']}PC{colors['fechador']})✌{colors['ciano']} x{colors['fechador']} 🤜 (VOCÊ)")
        print(f"{colors['GANHOU']}VOCÊ GANHOU{colors['fechador']}")
    elif pc == 2 and voce == 2:
        print(f"({colors['PC']}PC{colors['fechador']})✌ {colors['ciano']} x{colors['fechador']} ✌ (VOCÊ)")
        print(f"EMPATE")
    elif pc == 2 and voce == 3:
        print(f"({colors['PC']}PC{colors['fechador']})✌ {colors['ciano']} x{colors['fechador']} 🖖 ({colors['VOCÊ']}VOCÊ{colors['fechador']})")
        print(f"{colors['PC']}VOCÊ PERDEU{colors['fechador']}")
    elif pc == 3 and voce == 1:
        print(f"({colors['PC']}PC{colors['fechador']})🖖 {colors['ciano']} x{colors['fechador']} 🤜 ({colors['VOCÊ']}VOCÊ{colors['fechador']})")
        print(f"VOCÊ PERDEU")
    elif pc == 3 and voce == 2:
        print(f"({colors['PC']}PC{colors['fechador']})🖖 {colors['ciano']} x{colors['fechador']} ✌ ({colors['VOCÊ']}VOCÊ{colors['fechador']})")
        print(f"{colors['PC']}VOCÊ GANHOU{colors['fechador']}")
    elif pc == 3 and voce ==3:
        print(f"({colors['PC']}PC{colors['fechador']})🖖 {colors['ciano']} x{colors['fechador']} 🖖 ({colors['VOCÊ']}VOCÊ{colors['fechador']})")
        print(f"EMPATE")
    elif voce == 4:
        break
    else:
        print(f'{colors["PC"]}NÃO EXISTE ESSA OPÇÃO{colors["fechador"]}')
    
print("Até mais! 👋👋👋")