lista = input().split() #Entrada de valores na mesma linha separado por espaço
print()
lista = sorted(lista, key=int)
leng = len(lista)
i = -1
for cont in lista:
    if cont != leng:
        i = i +1
        print('Número %d:' % (i + 1), lista[i])
