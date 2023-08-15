from time import sleep
def contador(inicio, fim, passo):
    print(f'\nContagem de {inicio} à {fim} de {passo} em {passo}')
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            sleep(1)
            print(f'{cont} ', end='', flush='True')
            cont += passo
        print()
    else:
        cont = inicio
        while cont >= fim:
            sleep(1)
            print(f'{cont} ', end='', flush='True')
            cont -= passo
        print()


def lin():
    print('=-='*25)


lin()
contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
i = int(input('\nInsira o valor inicial: '))
f = int(input('Digite o valor final: '))
p = int(input('Insira o valor de progressão: '))

contador(i, f, p)
lin()
