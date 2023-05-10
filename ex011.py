larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
print('Sua parede com as medidas {} m e {} m possui uma área de {}m², e necessitará de {} L de tinta para ser totalmente pintada.' .format(larg, alt, larg*alt, (alt*larg)/2))
