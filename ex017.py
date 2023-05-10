import math

'''c1 = float(input('Digite um valor: '))
c2 = float(input('Digite outro valor: '))
h = (c1**2 + c2**2)**(1/2)
print('Um triângulo com os catetos {} e {} terá uma hipotenusa aproximada igual à {:.2f}.' .format(c1, c2, h))'''

co = float(input('Digite um valor: '))
ca = float(input('Digite outro valor: '))
hp = math.hypot(co, ca)
print('A hipotenusa é {:.2f}' .format(hp))
