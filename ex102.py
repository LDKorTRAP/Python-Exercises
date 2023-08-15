def fatorial(num, show = 0):
    """
    num -> número selecionado para o fatorial
    fact -> variável para acumular o resultado das sucessivas contas de fatorial
    c -> parâmetro numérico do fatorial
    """
    fact = num
    if show == True:
        print('-=-'*20)
        print(f'{num}! -> {num} ', end='')
        for c in range(num, 1, -1):
            fact *= (c - 1)
            print(f' * {c - 1}', end='')
        print(f' = {fact}')
    else:
        print('-=-'*20)
        for c in range(num, 1, -1):
            fact *= (c - 1)
        print(f'{num}! = {fact}')


fatorial(3, False)
fatorial(5, True)
fatorial(6, False)

help(fatorial)
