dist = float(input('Boa tarde! Informe a distância total da sua viagem: '))
if dist > 200:
    print('Sua viagem de {} Km irá começar.' .format(dist))
    print('A sua passagem ira custar um total de R$ {:.2f}.' .format(dist*0.45))
else:
    print('Sua viagem de {} Km irá começar.'.format(dist))
    print('A sua passagem irá custar um total de R$ {:.2f}.' .format(dist*.5))
