linhas = [[], [], []]
cont = 1
for c in range(1, 10):
    if c < 4:
        num = int(input(f'\033[35mInsira o valor para a posição [1, {cont}]:\033[m '))
        cont += 1
        linhas[0].append(num)
        if cont == 4:
            cont = 1

    if c > 3 and c < 7:
        num = int(input(f'\033[35mInsira o valor para a posição [2, {cont}]:\033[m '))
        cont += 1
        linhas[1].append(num)
        if cont == 4:
            cont = 1

    if c > 6:
        num = int(input(f'\033[35mInsira o valor para a posição [3, {cont}]:\033[m '))
        cont += 1
        linhas[2].append(num)

print('\033[31m=-=\033[m'*25)
print(f'\n\033[35mMatriz 3x3\033[m')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'\033[31m[{linhas[l][c]:^5}]\033[m', end='')
    print()