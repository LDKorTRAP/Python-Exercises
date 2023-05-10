from random import randint
from time import sleep
print('\033[1;33mBem vindo ao desafio de JoKenPo\033[m')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('\033[1;33mSuas opções:\033[m \n\033[36m[0] Pedra\033[m \n\033[35m[1] Papel\033[m \n\033[34m[2] Tesoura\033[m')
jogador = int(input('Qual a sua jogada? '))
print('\033[1;33m=-=\033[m'*10)
print('\033[35mJO\033[m')
sleep(2)
print('\033[35mKEN\033[m')
sleep(2)
print('\033[35mPO\033[m')
print('\033[1;33m=-=\033[m'*10)
print('\033[36mComputador jogou {}.\033[m' .format(itens[computador]))
print('\033[35mJogador jogou {}.\033[m' .format(itens[jogador]))
print('\033[1;33m=-=\033[m'*10)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('\033[1;31mJogada inválida\033[m')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('\033[1;31mJogada inválida\033[m')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('\033[1;31mJogada inválida\033[m')
