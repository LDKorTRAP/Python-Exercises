nome = str(input('Qual o seu nome, my lord? ')).strip()
print('Devo me referir a vossa exelência como:')
print(nome.upper())
print(nome.lower())
print('Seu primeiro nome detem {} letras.' .format(nome.find(' ')))
print('Seu nome ao todo possui {} letras.' .format(len(nome)-nome.count(' ')))