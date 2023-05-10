print('Bem vindo(a) a pesquisa de saúde pública da ilha! Vamos calcular seu IMC.')
peso = float(input('Digite aqui seu peso atual: '))
altura = float(input('Digite aqui sua altura: '))
IMC = peso/(altura)**2
if IMC < 18.5:
    print('Seu IMC é atualmente {:.1f}, você está abaixo do peso.' .format(IMC))
elif IMC < 25:
    print('Seu IMC é atualmente {:.1f}, você está no peso ideal.' .format(IMC))
elif IMC < 30:
    print('Seu IMC é atualmente {:.1f}, você está acima do peso.' .format(IMC))
elif IMC < 40:
    print('Seu IMC é atualmente {:.1f}, você está em fase de obesidade.' .format(IMC))
else:
    print('Seu IMC é atualmente {:.1f}, você está em fase de obesiade mórbida.' .format(IMC))
