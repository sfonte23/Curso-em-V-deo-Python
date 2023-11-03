'''print("="*22)
print("Sequência de Fibonacci")
print("="*22)

termos  = int(input("\nQuantos termos você quer mostrar? "))
contador = 1
posterior = 1
anterior = 0
termos-2
print("~~"*10)
print("0, 1, ",end="")
while contador < termos:
    auxiliar = posterior
    posterior += anterior
    anterior = auxiliar
    contador += 1
    print(f"{posterior}, ",end='')

print("FIM!")

'''
n = int(input("Quantos termos deseja visualizar? "))
t1 = 0
t2 = 1

print(f"{t1} -> {t2}",end="")
cont = 3
while cont <= n:
    t3 = t1+t2
    print(f" -> {t3}", end="")
    t1=t2
    t2=t3
    cont +=1
print("-> FIM")