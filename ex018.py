import math
n = float(input('Escreva um valor para um ângulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tag = math.tan(math.radians(n))
print('O ângulo de {:.0f}° possui \nSeno = {:.2f} \nCosseno = {:.2f} \nTangente = {:.2f}' .format(n, sen, cos, tag))
