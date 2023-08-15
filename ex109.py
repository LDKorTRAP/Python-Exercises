from modulos import moeda109

n = float(input('Insira um valor em R$ '))

moeda109.aumentar(n)
print(f'Aumentando 10% do valor {moeda109.moeda(n)}, se torna {moeda109.aumentar(n)}')
moeda109.diminuir(n)
print(f'Diminuindo 10% do valor {moeda109.moeda(n)}, se torna {moeda109.diminuir(n)}')
moeda109.dobro(n)
print(f'O dobro do valor {moeda109.moeda(n)} será {moeda109.dobro(n)}')
moeda109.metade(n)
print(f'A metade do valor {moeda109.moeda(n)} será {moeda109.metade(n)}')
