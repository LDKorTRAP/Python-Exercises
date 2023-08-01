lista = (int(input('Insira um valor: ')), int(input('Insira um valor: ')), int(input('Insira um valor: ')), int(input('Insira um valor: ')))
print(f'O número 9 apareceu {lista.count(9)}.')
if 3 in lista:
    print(f'O número 3 apareceu na posição {lista.index(3) + 1}.')
else:
    print('Não houve aparição do número 3.')
print('Os valores pares digitados foram: ', end='')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')