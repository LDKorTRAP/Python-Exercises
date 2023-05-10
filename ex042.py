print('\033[1;31mBora fazer um triângulo!\033[m')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))
n3 = int(input('Digite outro número inteiro: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n3 + n2 > n1:
    print('\033[1;36mAqui nos temos um belíssimo triângulo.\033[m')
else:
    print('\033[1;31mEsses valores não servem pra um triângulo, meu querido.\033[m')
    exit()
if n1 == n2 == n3:
    print('Seu triângulo é \033[1;35mequilátero\033[m.')
elif n1 == n2 and n1 != n3:
    print('Seu triângulo é \033[1;34misóceles\033[m.')
elif n1 == n3 and n1 != n2:
    print('Seu triângulo é \033[1;34misóceles\033[m.')
elif n2 == n3 and n2 != n1:
    print('Seu triângulo é \033[1;34misóceles\033[m.')
elif n2 != n1 and n1 != n3 and n2 != n3:
    print('Seu triângulo é \033[1;33mescaleno\033[m.')
