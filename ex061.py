print('gerador de PA')
print('=-=' * 20)
num = int(input('Insira o primeiro termo: '))
raz = int(input('Insira a razão da progressão: '))
cont = 1
while cont <= 10:
    print('{}' .format(num), end='')
    print(' → ', end='')
    num = num + raz
    cont += 1
print('Fim')