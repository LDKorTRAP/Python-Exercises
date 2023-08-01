saque = ced1 = ced10 = ced20 = ced50 = 0
num = -1
print('\033[1:36m-\033[m'*25)
print('\033[4:30:44mBem vindo ao Banco Tritão\033[m')
print('\033[1:36m-\033[m'*25)
while num <= 0:
    num = int(input('\033[1:34mDigite um valor inteiro a ser sacado:\033[m '))
    if num <= 0:
        print('\033[1:31mInsira um valor válido! (valor > 0)\033[m')
saque = num
while saque != 0:
    while saque >= 50:
        saque -= 50
        ced50 += 1
    while saque >= 20:
        saque -= 20
        ced20 += 1
    while saque >= 10:
        saque -= 10
        ced10 += 1
    while saque > 0:
        saque -= 1
        ced1 += 1
    if saque <= 0:
        break
if ced50 > 0:
    print(f'\033[1:34mCédulas de R$ 50: {ced50}\033[m')
if ced20 > 0:
    print(f'\033[1:36mCédulas de R$ 20: {ced20}\033[m')
if ced10 > 0:
    print(f'\033[1:34mCédulas de R$ 10: {ced10}\033[m')
if ced1 > 0:
    print(f'\033[1:36mCédulas de R$ 1: {ced1}\033[m')

