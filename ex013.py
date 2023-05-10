sal = float(input('Qual o salário o seu funcionário? R$'))
new = sal+(sal*0.15)
print('O salário base era de R${:.2f}, e passará a ser R${:.2f}, mediante um aumento de 15%.' .format(sal, new))
