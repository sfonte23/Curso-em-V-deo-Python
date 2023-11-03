''' Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e 
mostre uma mensagem com tamanho adaptável.'''
def escreva(txt):
    tam = len(txt)+4
    print(f'~'*tam)
    print(f'  {txt}')
    print(f'~'*tam)

escreva('CeV')
escreva('Olá Mundo')
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')