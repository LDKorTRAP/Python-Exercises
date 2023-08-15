#nums = list()
#print('\033[31mListagem Numérica\033[m')
#def maior():
#    while True:
#
#        nums.append(int(input('\n\033[35mInsira um novo valor:\033[m ')))
#
#        while True:
#            resp = str(input('\033[35mDeseja continuar? (S/N)\033[m '))
#            if resp in 'SsNn':
#                break
#            else:
#                print('\033[1;31mInsira uma opção válida!\033[m')
#
#        if resp in 'Nn':
#            break
#    m = 0
#    for c in range(0, len(nums)):
#        if nums[c] >= m:
#          m = nums[c]
#   nums.sort()
#   print(f'\n\033[35mO maior número registrado da lista\033[m \033[31m{nums}\033[m \033[35mfoi\033[m \033[31m{m}\033[m')


#maior()

from time import sleep
def maior(*num):
    mr = 0
    for valor in num:
        if mr == 0:
            mr = valor
        else:
            if valor > mr:
                mr = valor
    print('\033[34mAnalisando valores:\033[m ')
    for p in num:
        sleep(.5)
        print(f'\033[35m{p}\033[m ', end='', flush='True')
    print(f'\nO maior valor foi {mr}.')
    print('\033[34m-=-\033[m'*20)


maior(1, 5, 8, 4)
maior(250, 10)
maior(-100, -50, 0)
