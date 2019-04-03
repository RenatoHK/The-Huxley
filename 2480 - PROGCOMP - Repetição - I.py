base = float(input())
exp = int(input())
res = 0
total = 1

for i in range(exp):
    res = (total * base)
    total = res  
print('%.2f' % total)
