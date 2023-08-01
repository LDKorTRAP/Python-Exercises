option = str('maybe')
preço = total = contMIL = 0
barato = 1000000
cheap = str('sim')
produto = str('produto')

print('\033[1:36m-\033[m'*20)
print('\033[4:35mMercadinho Levignus\033[m')
print('\033[1:36m-\033[m'*20)

while option != 'N':
    produto = str(input('\033[1:36mProduto: \033[m '))
    preço = float(input('\033[1:36mPreço: R$ \033[m '))
    total += preço
    if preço < barato:
        barato = preço
        cheap = produto
    if preço > 1000:
        contMIL += 1
    option = str(input('\033[1:35mDeseja continuar? (S/N)\033[m ')).upper()
    if option == 'N':
        break
print(f'\n\033[1:36mTotal gasto: R$ {total:.2f} \nTotal de produtos acima de R$ 1000: {contMIL} \nProduto mais barato: {cheap}, R$ {barato:.2f}\033[m')