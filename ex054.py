import datetime
cont1 = 0
cont2 = 0
atual = datetime.date.today().year
for c in range(1,8):
    nascimento = int(input('Digite a data de nascimento: '))
    idade = atual - nascimento
    if idade >= 18:
        cont1 += 1
    else:
        cont2 += 1
print('O número de maiores de idade é {}, e o de menores de idade é {}.' .format(cont1, cont2))
