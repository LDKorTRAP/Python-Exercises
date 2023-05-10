from datetime import date
n1 = int(input('Digite um ano qualquer (digite 0 para o atual): '))
if n1 == 0:
    n1 = date.today().year
if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('O ano de {} é um ano bissexto.' .format(n1))
else:
    print('O ano de {} não é um ano bissexto.' .format(n1))
