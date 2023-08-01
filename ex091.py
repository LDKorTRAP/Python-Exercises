import random, time
from operator import itemgetter
jogadores = {}
ranking = {}

print('\033[34mOH BOA NOITE!\033[m')
time.sleep(2)
print('\033[34mHOJE, 4 jogadores para disputar o prêmio de 100.000 dilmas. São eles: Lily, Sad, Ira e Hen!\033[m')
time.sleep(2)
print('\033[31mE eles já estão lançando seus dados!\033[m\n')

jogadores['Lily'] = random.randint(1, 6)
jogadores['Ira'] = random.randint(1, 6)
jogadores['Sad'] = random.randint(1, 6)
jogadores['Hen'] = random.randint(1, 6)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
time.sleep(1)
print('\033[35m=-=\033[m'*15)
print('\n\033[31mE os resultados foram:\033[m')

for p, n in jogadores.items():
    time.sleep(1)
    print(f'\033[35m{p} tirou\033[m \033[31m{n}\033[m')

print('\n\033[31mRanking Final\033[m')
for i, v in enumerate(ranking):
    print(f'\033[35m{i+1}º Lugar: {v[0]} com nº\033[m \033[31m{v[1]}\033[m')
