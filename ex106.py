c = ('\033[m', #no color
     '\033[0;30;41m', #red
     '\033[0;;42m', #green
     '\033[0;;43m', #yellow
     '\033[0;;44m', #blue
     '\033[0;;45m', #purple
     );
def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')


def título(msg, cor = 0):
    tamanho = len(msg)
    print(c[cor], end='')
    print('='*tamanho)
    print(msg)
    print('='*tamanho)
    print(c[0], end='   ')


comando = ''
while True:
    título('Sistema de Ajuda Pyhelp', 2)
    comando = str(input("Função ou Biblioteca: "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('FINALIZANDO SISTEMA', 1)
