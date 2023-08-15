def aumentar(preço = 0, t1 = 0, moeda = 'R$'):
    valor = preço + (preço*t1/100)
    return print(f'{t1}% de aumento: \t{moeda}{valor:>.2f}'.replace('.', ','))


def diminuir(preço = 0, t2 = 0, moeda = 'R$'):
    valor = preço - (preço*t2/100)
    return print(f'{t2}% de redução: \t{moeda}{valor:>.2f}'.replace('.', ','))


def dobro(preço = 0, moeda = 'R$'):
    valor = preço * 2
    return print(f'Dobro do valor: \t{moeda}{valor:>.2f}'.replace('.', ','))


def metade(preço = 0, moeda = "R$"):
    valor = preço/2
    return print(f'Metade do valor: \t{moeda}{valor:>.2f}'.replace('.', ','))


def moeda(preço = 0, moeda = 'R$'):
    return print(f'Moeda analisada: \t{moeda}{preço:>.2f}'.replace('.', ','))


def resumo(n, t1, t2):
    print('-'*35)
    print('VALORES'.center(35))
    print('-'*35)
    moeda(n)
    aumentar(n, t1)
    diminuir(n, t2)
    dobro(n)
    metade(n)
    print('-'*35)
    