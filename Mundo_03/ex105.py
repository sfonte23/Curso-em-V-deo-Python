''' Faça um programa que tenha uma função notas() 
que pode receber várias notas de alunos 
e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)'''

def notas (*n,sit=False):
    """-> Função para analisr notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a sitauação
    :return: dicionário com várias informações sobre a situação da turma
    """
    notas = {}
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['média'] = sum(n)/len(n)
    if sit:
        if notas['média'] >=7:
            notas['situação'] = 'BOA'
        elif notas['média'] >= 5:
            notas['situação'] = 'RAZOÁVEL'
        else:
            notas['situação'] = 'RUIM'
    return notas



#Programa Principal
resp = notas(5.5,9.5,10,6.5,sit=True)
print(resp)