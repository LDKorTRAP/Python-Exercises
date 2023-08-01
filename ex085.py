nums = [[], []]

for c in range(1,8):
    num = int(input(f'\033[34mInsira o {c}º valor:\033[m '))
    print('\033[35m+\033[m'*25)
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)

nums[0].sort()
nums[1].sort()

print(f'\n\033[35mTodos os valores:\033[m \033[34m{nums}\033[m \n\033[35mValores pares:\033[m \033[34m{nums[0]}\033[m \n\033[35mValores ímpares:\033[m \033[34m{nums[1]}\033[m')
