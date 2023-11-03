def leiaDinheiro(msg):
    validador = False
    while not validador:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha():
            print(f'\033[31mERRO! \"{entrada}\" não é um preço válido.\033[m')
        else:
            validador = True
            return float(entrada)