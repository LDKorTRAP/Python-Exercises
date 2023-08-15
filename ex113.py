def leiaint(msg):
    ok = False
    valor = 0
    while True:
        try:
            i = int(input(msg))
            valor = int(i)
            ok = True
            break
        except (TypeError, ValueError):
            print('\033[1;31mERRO, INSIRA UM VALOR VÁLIDO\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida!\033[m')
            return 0
    return valor


def leiafloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            r = float(input(msg))
            valor = float(r)
            ok = True
            break
        except (TypeError, ValueError):
            print('\033[1;31mERRO, INSIRA UM VALOR VÁLIDO\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida!\033[m')
            return 0
    return valor


i = leiaint('\nDigite um número inteiro: ')
r = leiafloat('\nDigite um valor real: ')
print(f'Você digitou o número inteiro {i} e o número real {r}')
