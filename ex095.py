time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('\nNome: '))
    tot = int(input('Partidas: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Gols feitos na {c+1}ª partida: ')))
    jogador['gols'] = partidas[:]
    jogador['saldo'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Deseja continuar? (S/N) '))
        if resp in 'SsNn':
            break
        else:
            print('ERROR! Insira apenas S ou N!')
    if resp in 'Nn':
        break

print('+=+'*25)
print('Cod.', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
     print(f'\n{k:>3} ', end='')
     for d in v.values():
        print(f'{str(d):<15}', end='')
print()
print('+=+'*25)

while True:
    busca = int(input('\nQual jogador deseja ver? (999 para finalizar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERROR! Não existe o jogador com código {busca}!')
    else:
        print( f'--Dados do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} ele fez {g} gols.')
    print('+=+'*25)
