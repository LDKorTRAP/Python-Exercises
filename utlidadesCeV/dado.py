def dinheiro(msg):
    val = False
    while not val:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print('\033[31mIsso não é um valor válido, tente novamente!\033[m')

        else:
            val = True
            return float(n)
