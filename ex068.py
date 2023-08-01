import random
dec = 'maybe'
option = 'maybe'
num = 0
numPC = 0
contV = 0
while option != 'perdeu':
    dec = str(input('Impar ou par? ')).lower()
    num = int(input('Digite seu número escolhido: '))
    numPC = random.randint(1, 11)
    print(f'Você jogou {num} e o computador jogou {numPC}, resultou {num+numPC}')
    if dec == 'par' and (num+numPC) % 2 == 0:
        print('Você ganhou!')
        contV += 1
        option = 'ganhou'
    elif dec == 'impar' and (num+numPC) % 2 != 0:
        print('Você ganhou!')
        contV += 1
        option = 'ganhou'
    else:
        print('Você perdeu!')
        break
print(f'Seu total de vitórias foi de {contV}')
