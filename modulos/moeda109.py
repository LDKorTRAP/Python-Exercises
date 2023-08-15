def aumentar(preço = 0, taxa = 10, moeda = 'R$'):
    valor = preço + (preço*taxa/100)
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def diminuir(preço = 0, taxa = 10, moeda = 'R$'):
    valor = preço - (preço*taxa/100)
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def dobro(preço = 0, moeda = 'R$'):
    valor = preço * 2
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def metade(preço = 0, moeda = "R$"):
    valor = preço/2
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')
