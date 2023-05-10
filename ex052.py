print('\033[1;33mDetector de número primos\033[m')
n1 = int(input('\033[33mDigite um número: '))
cont = 0
for c in range(1,n1 +1):
    if n1 % c == 0:
        print('\033[34m', end=' ')
        cont = cont + 1
    else:
        print('\033[31m', end=' ')
    print('{}' .format(c), end=' ')
print('\n\033[33mO número {} foi dividido {} vezes.' .format(n1, cont))
if cont == 2:
    print('O número {} é primo.' .format(n1))
else:
    print('O número {} não é primo.' .format(n1))
