print('PLIN PLIN! Radar logo mais a frente!')
v1 = float(input('Digite a sua velocidade atual: '))
v2 = 80
v3 = v1 - v2
multa = v3*7
if v1 > 80:
    print('EI EI! Você está acima do limite da via! Será multado em um total de R$ {:.0f}.' .format(multa))
else:
    print('Sua velocidade está dentro do limite da via de 80km/h. Boa viagem.')
