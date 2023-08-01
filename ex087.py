matriz = [[], [], []]
cont = 1
pares = 0
maior = 0

for c in range(1,10):
    if c < 4:
        num = int(input(f'Insira o valor para [1, {cont}]: '))
        cont += 1
        matriz[0].append(num)
        if num % 2 == 0:
            pares += num
        if cont == 4:
            cont = 1

    elif c > 3 and c < 7:
        num = int(input(f'Insira o valor para [2, {cont}]: '))
        matriz[1].append(num)
        if num % 2 == 0:
            pares += num
        cont += 1
        if cont == 4:
            cont = 1
        if num > maior:
            maior = num

    else:
        num = int(input(f'Insira o valor para [3, {cont}]: '))
        matriz[2].append(num)
        cont += 1
        if num % 2 == 0:
            pares += num


print('\nMatriz 3x3')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'Somatórios dos números pares digitados: {pares}')
print(f'Maior número da linha 2: {maior}')