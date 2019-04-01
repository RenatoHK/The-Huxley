num = []
n = 0
carros = 0
total = 0
while n != 999:
    n = int(input())
    if n !=999:
        num.append(n)
for k in range(len(num)):
    qtd = num[k]
    if qtd > 2:
        carros = carros + (qtd - 2)
        total += 1
print('%.2f' % (carros * 12.89), )
print(total)
