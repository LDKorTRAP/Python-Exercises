from random import randint
from time import sleep
nums = list()

def sorteia():
    print('Sorteando números')
    for c in range(0, 5):
        nums.append(int(randint(0, 100)))
        sleep(.5)
        print(f'{nums[c]} ', end='', flush=True)

    nums.sort()
    print(f'\nValores sorteados: {nums}')


def somaPar():
    pares = 0
    for c in nums:
        if c % 2 == 0:
            pares += c
    print(f'A soma dos valores pares totalizou: {pares}')


sorteia()
somaPar()
