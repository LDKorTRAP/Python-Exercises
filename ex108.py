from modulos import moeda108

n = float(input('Insira um valor em R$ '))

moeda108.aumentar(n)
print(f'Aumentando 10% do valor {moeda108.moeda(n)}, se torna {moeda108.moeda(moeda108.aumentar(n))}')
moeda108.diminuir(n)
print(f'Diminuindo 10% do valor {moeda108.moeda(n)}, se torna {moeda108.moeda(moeda108.diminuir(n))}')
moeda108.dobro(n)
print(f'O dobro do valor {moeda108.moeda(n)} será {moeda108.moeda(moeda108.dobro(n))}')
moeda108.metade(n)
print(f'A metade do valor {moeda108.moeda(n)} será {moeda108.moeda(moeda108.metade(n))}')
