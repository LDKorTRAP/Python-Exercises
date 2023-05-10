n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O primeiro valor, {}, é o maior' .format(n1))
elif n1 < n2:
    print('O segundo valor, {}, é o maior' .format(n2))
else:
    print('Os dois valores são iguais, logo não há maior')
