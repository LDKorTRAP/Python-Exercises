n1 = float(input('Digite o valor do salário do funcionário: R$ '))
if n1 > 1250:
    print('O salário receberá um aumento de 10%, passando a ser totalizado em R$ {:.2f}' .format(n1+(n1*.1)))
else:
    print('O salário receberá um aumento de 15%, passando a ser totalizado em R$ {:.2f}' .format(n1+(n1*.15)))
