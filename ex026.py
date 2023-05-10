frase = str(input('Digite uma frase: ')).strip()
print('Nesta frase digitada: \nletra A aparecendo {} vezes.' .format(frase.upper().count('A')))
print('O primeiro A apareceu na posição {}.' .format(frase.lower().find('a')+1))
print('O último A aparece na posição {}.' .format(frase.lower().rfind('a')+1))
