print('Classificação Série B do Brasileirão')
chapeco = 'sim'
cont = 0
serieB = ['cruzeiro', 'grêmio', 'bahia', 'vasco da gama', 'sampaio corrêa', 'ituano', 'sport recife', 'criciúma', 'londrina', 'guarani', 'crb', 'ponte preta', 'vila nova', 'chapecoense', 'tombense', 'novorizontino', 'csa', 'brusque', 'operário', 'náutico']
print(f'5 primeiros colocados: {serieB[0]}, {serieB[1]}, {serieB[2]}, {serieB[3]}, {serieB[4]}')
print('=-='*30)
print(f'4 últimos colocados: {serieB[16]}, {serieB[17]}, {serieB[18]}, {serieB[19]}')
print('=-='*30)
serieB.sort(reverse=False)
print(f'Ordem Alfabética: {serieB}')
print('=-='*20)
while chapeco != 'chapecoense':
    chapeco = serieB[cont]
    cont += 1

print(f'A Chapecoense acabou na posição {cont}')
