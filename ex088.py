import random, time

megasena = list()
nums = list()
sec = 1
limite = 7

jogos = int(input('\033[35mQual o número de jogos?\033[m '))


while sec <= jogos:
    cont = 0
    while True:
        sorteado = random.randint(1, 60)
        if sorteado not in nums:
            nums.append(sorteado)
            cont += 1
        if cont >= 6:
            break
    nums.sort()
    megasena.append(nums[:])
    nums.clear()
    sec += 1

print('\n\033[34mNúmeros sorteados\033[m')

cont = 0

for c in range(0, jogos):
    time.sleep(2)
    print(f'\033[35mJogo {cont + 1}: {megasena[cont]}\033[m')
    cont += 1

print('\033[34m----- Good Luck, Honey -----\033[m')