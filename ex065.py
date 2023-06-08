num = cont = maior = menor = media = 0
option  = str('MAYBE')
while option != 'N':
    num = int(input('\nDigite um número inteiro: '))
    option = str(input('Deseja continuar? (S/N) ')).upper()
    cont += 1
    media += num
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
media = media/cont
print('\nMédia: {} \nMaior número digitado: {} \nMenor número digitado: {}' .format(media, maior, menor))
