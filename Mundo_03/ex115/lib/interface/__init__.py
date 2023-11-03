
cf =['\033[31m',   # [0] vermelho
        '\033[32m',   # [1] verde
        '\033[34m',   # [2] azul
        '\033[36m',   # [3] ciano
        '\033[35m',   # [4] magenta
        '\033[33m',   # [5] amarelo
        '\033[30m',   # [6] preto
        '\033[m']     # [7] normal

def leiaInt(txt):
        while True:
            try:
                n=int(input(txt))
            except (ValueError, TypeError):
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
                continue
            except (KeyboardInterrupt):
                 print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
                 return 0
            else:
                 return n

def entrada(lista):
    print('-'*30)
    print(f'{"MENU":^30}')
    print('-'*30)
    c=1
    for item in lista:
        print(f'{cf[5]}{c}{cf[7]} - {cf[2]}{item}{cf[7]}')
        c+=1
    print('-'*30)
    opc = leiaInt(f'{cf[4]}Sua Opção:{cf[7]} ')
    return opc
