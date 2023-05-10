l1 = float(input('Primeiro valor: '))
l2 = float(input('Segundo Valor: '))
l3 = float(input('Terceiro valor: '))
if l1 < l2 + l3 and l2 <l1 + l3 and l3 < l1 + l2:
    print('Os valores {}, {} e {} formam um triângulo.' .format(l1, l2, l3))
else:
    print('Os valores {}, {} e {} não podem formar um triângulo.' .format(l1, l2, l3))
