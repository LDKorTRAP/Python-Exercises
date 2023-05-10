from time import sleep
print('\033[1;35mBem vindo ao caixa rápido da Saga Duaragons\033[m')
valor = float(input('\033[35mDigite aqui o valor do seu produto:\033[m '))
print('\033[35mNossa loja oferece os seguintes tipos de pagamentos:\033[m \033[36m\n[1] A vista no dinheiro ou cheque \n[2] A vista no cartão \n[3] Parcelado em duas vezes no cartão \n[4] Parcelado em 3 vezes ou mais no cartão\033[m')
pagamento = int(input('\033[35mQual será a forma de pagamento escolhida?\033[m '))
if pagamento == 4:
    parcelas = int(input('\033[35mSerão quantas parcelas?\033[m '))
print('\033[1;36mProcessando o código de barras\033[m \033[1;30;107m││ │|│ │| │||| ││||│\033[m')
sleep(5)
if pagamento == 1:
    print('O valor final da sua compra a vista no dinheiro será de R$ {:.2f}.' .format(valor-(valor*.1)))
elif pagamento == 2:
    print('O valor final da sua compra no cartão de débito será de R$ {:.2f}.' .format(valor-(valor*.05)))
elif pagamento == 3:
    print('O valor final de seu produto será de duas parcelas de R$ {:.2f}, sem acréscimo de juros.' .format(valor/2))
elif pagamento == 4:
    print('O valor final de seu produto será de {} parcelas de R$ {:.2f}, totalizando R$ {:.2f}, com o acréscimo do juros.' .format(parcelas, (valor*.2+valor)/parcelas, (valor*.2+valor)))
else:
    print('\033[1;31mPor favor, selecione uma das formas de pagamento entregues acima.\033[m')
