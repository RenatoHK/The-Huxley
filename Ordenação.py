
n1 = int(input('Insira um numero com 4 digitos: '))

r1 = n1 % 10
r2 = (n1 // 10) % 10
r3 = (n1 // 100) % 10
r4 = (n1 // 1000) % 10
print(r1, end='')
print(r2, end='')
print(r3, end='')
print(r4, end='')
