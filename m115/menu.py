from time import sleep
from m115.arquivo import *
def menu():
    while True:
        estrutura()
        try:
            option = int(input('\033[33mSua opção:\033[m '))
            if option == 1:
                sleep(1)
                visualizar()
            elif option == 2:
                sleep(1)
                registrar()
            elif option == 3:
                linhas()
                print(f'\033[1;31m{"FINALIZANDO SISTEMA":^30}\033[m')
                linhas()
                sleep(1)
                break
            else:
                print('\033[1;31mERROR: Insira uma opção válida!\033[m')
        except:
            print('\033[1;31mERROR: Insira um valor numérico inteiro.\033[m')
        

def estrutura():
    sleep(1)
    linhas()
    print(f'\033[34m{"MENU PRINCIPAL":^30}\033[m')
    linhas()
    print('\033[33m1 - Ver pessoas cadastradas \n2 - Cadastrar nova pessoa \n3 - Sair do Sistema\033[m')
    linhas()


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


def visualizar():
    linhas()
    print(f'\033[34m{"PESSOAS CADASTRADAS":^30}\033[m')
    linhas()
    lerArquivo('cursoemvideo.txt')


def registrar():
    linhas()
    print(f'\033[34m{"NOVO CADASTRO":^30}\033[m')
    linhas()
    nome = str(input('Nome: '))
    idade = leiaint('Idade: ')
    cadastrar('cursoemvideo.txt', nome, idade)


def linhas():
    print('\033[35m-\033[m'*30)
