print('\033[1;31m=\033[1;35m '*13)
print('\033[1;35m10 primeiros termos da PA\033[m')
print('\033[1;31m=\033[1;35m '*13)
base = int(input('Qual o primeiro número? '))
raz = int(input('Qual a razão? '))
décimo = base + (10-1)*raz
for c in range(base,décimo +raz, raz):
    print(c, end=' ')
