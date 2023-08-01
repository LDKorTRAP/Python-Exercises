temporada = {}
gols = []
saldo = 0
cont = 1

temporada['Jogador'] = str(input('Nome do jogador: '))
temporada['Partidas'] = int(input('Total de partidas: '))

for g in range(0, temporada['Partidas']):
    gols.append(int(input(f'Gols feitos na partida {g+1}: ')))
    saldo += gols[g]

temporada['gols'] = gols
temporada['Saldo'] = saldo
print('+-+'*15)
print(temporada)

print('\n--- Temporada ---')
print(f'\nJogador: {temporada["Jogador"]} \nPartidas: {temporada["Partidas"]}\n')
for p in temporada['gols']:
    print(f'Partida {cont}: {p} gols')
    cont += 1
print(f'Saldo: {temporada["Saldo"]}')