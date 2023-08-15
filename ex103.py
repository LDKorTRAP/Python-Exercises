def ficha(nome = '<Desconhecido>', gols = 0):
    print(f'O jogador {nome} marcou um total de {gols} gols')


n = str(input('Jogador: '))
g = str(input('Gols feitos: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
