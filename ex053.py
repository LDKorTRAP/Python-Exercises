frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('A sua frase {} invertida fica {}.' .format(junto, inverso))
if inverso == junto:
    print('A sua frase é um palíndromo.')
else:
    print('A sua frase não é um palíndromo.')
