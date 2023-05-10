n = int(input('Digite um número inteiro qualquer: '))
print("""Escolha o caminho de conversão do número:
\033[1;34m[1]Binário\033[m
\033[1;33m[2]Octal\033[m
\033[1;32m[3]Hexadecimal\033[m""")
option = int(input('Digite o número da escolha: '))
if option == 1:
    print('{} convertido para \033[34mbinário\033[m é \033[34m{}\033[m' .format(n, bin(n)[2:]))
elif option == 2:
    print('{} convertido para \033[33moctal\033[m é \033[33m{}\033[m' .format(n, oct(n)[2:]))
elif option == 3:
    print('{} convertido para \033[32mhexadecimal\033[m é \033[32m{}\033[m' .format(n, hex(n)[2:]))
else:
    print('\033[1;31mOpção inválida.\033[m')
