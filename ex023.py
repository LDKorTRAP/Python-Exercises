n1 = int(input('Digite um número entre 0 e 9999: '))
u = n1//1%10
d = n1//10%10
c = n1//100%10
m = n1//1000%10
print('Seu número atual, {}, possui:' .format(n1))
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}' .format(u, d, c ,m))
