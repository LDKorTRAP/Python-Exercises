preço = float(input('Digite o valor da mercadoria: R$'))
print('Olha a leitora: BIP BUP BIP BUP')
desc = preço-(preço*0.05)
print('Seu produto custa R${:.2f}, mas receberá 5% de desconto, passando a custar R${:.2f}.' .format(preço, desc))
