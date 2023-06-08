nume = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
zeplin = nume
cont = 1
total = 0
terms = 10
while(terms != 0):
    total = total + terms
    while(cont <= total):
        print('{} —> '.format(zeplin), end='')
        cont += 1
        zeplin += raz
    print('PAUSA')
    terms = int(input('\nQuantos termos a mais devem ser mostrados? '))
print('\nFinalizando programa!')