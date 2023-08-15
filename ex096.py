def area(l1, l2):
    area = l1 * l2
    print(f'\033[34mO terreno de comprimento {l1} m e largura {l2} m possui área total de {area} m²\033[m')
    lin()


def lin():
    print('\033[35m-+-\033[m'*25)
    

#programa principal
lin()
print('\033[1;35mCalculadora de área\033[m')
l1 = float(input('\033[34mComprimento do terreno:\033[m '))
l2 = float(input('\033[34mLargura do terreno:\033[m '))
lin()
area(l1, l2)
