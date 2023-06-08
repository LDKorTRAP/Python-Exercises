num = int(input('Insira um número inteiro positivo: '))
cont = num
fat = 1
print('calculando {}! = ' .format(num), end='')
while cont > 0:
    print('{}' .format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print('{}' .format(fat))
