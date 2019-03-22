sal = float(input('INSIRA O SALARIO: '))

if sal <= 1903.98:
    print('ISENTO')
elif sal <= 2826.65:
    print('TAXA 7,5%\n' + 'IMPOSTO DE: %.2f' % (sal * 0.075))
elif sal <= 3751.05:
    print('TAXA 15%\n' + 'IMPOSTO DE: %.2f' % (sal * 0.15))
elif sal <= 4664.68:
    print('TAXA 22,5%\n' + 'IMPOSTO DE: %.2f' % (sal * 0.225))
else:
    print('TAXA 27,5%\n' + 'IMPOSTO DE: %.2f' % (sal * 0.275))
