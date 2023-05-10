n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))
option = 0
while option != 5:
    option = int(input("""\nEscolha uma das operações abaixo (número): 
        (1)- Somar
        (2)- Multiplicar
        (3)- maior
        (4)- Novos números
        (5)- Sair do programa
        
        Opção: """))
    if option == 1:
        soma = n1+n2
        print('\nA soma de {} e {} resultou em {}.\n' .format(n1, n2, soma))
        print("=:=" * 30)
    elif option == 2:
        mult = n1*n2
        print('\nA multiplicação entre {} e {} resultou em {}.\n' .format(n1, n2, mult))
        print("=:=" * 30)
    elif option == 3:
        if n1 > n2:
            print('\n{} é o maior valor.\n' .format(n1))
            print("=:=" * 30)
        elif n1 < n2:
            print('\n{} é o maior valor.\n' .format(n2))
            print("=:=" * 30)
        else:
            print('\nNão há valor maior, pois ambos são iguais.\n')
            print("=:=" * 30)
    elif option == 4:
        n1 = float(input('\nInsira o primeiro valor: '))
        n2 = float(input('\nInsira o segundo valor: '))
    else:
        print('\nInsira uma opção válida!\n')
if option == 5:
    print('\nSaindo do programa!')
    print("=:=" * 30)
    exit(5)
