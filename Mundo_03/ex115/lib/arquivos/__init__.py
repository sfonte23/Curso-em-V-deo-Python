def arquivoExiste(nome):
    try:
        a = open(f'c:/Users/smfon/Desktop/Python/Curso-em-Vídeo-Python/Mundo_03/ex115/lib/arquivos/{nome}','rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print(f'Houve um ERRO na criação do Arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a= open(f'c:/Users/smfon/Desktop/Python/Curso-em-Vídeo-Python/Mundo_03/ex115/lib/arquivos/{nome}','rt')
    except:
        print('Houve um ERRO ao abrir o Arquivo!')
    else:
        print('-'*30)
        print('    PESSOAS CADASTRADAS')
        print('-'*30)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        a.close()
    
def cadastrar(arq,nome='<desconhecido>',idade=0):
    try:
        a= open(f'c:/Users/smfon/Desktop/Python/Curso-em-Vídeo-Python/Mundo_03/ex115/lib/arquivos/{arq}','at')
    except:
        print('Houve um ERRO na abertura do Arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
             print('ERRO ao escrever no Arquivo!')
        else:
            print(f'\033[32mNovo registro de {nome} adicionado com sucesso\033[m')
            a.close()
            