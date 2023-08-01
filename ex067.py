num = cont = 0
while num >= 0:
    cont = 0
    num = int(input('\nA tabuada deverá ser de qual número: '))
    if num < 0:
        break
    while cont <= 10:
        cont += 1
        if cont == 11:
            break
        print(f'{num} x {cont} = {cont*num}')
print('\nEncerrando programa!')