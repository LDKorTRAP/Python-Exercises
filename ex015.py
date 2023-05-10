km = float(input('Digite a quilometragem total percorrida com o carro: '))
tempo = int(input('Digite o total de dias em que o carro foi utilizado: '))
km2 = km*0.15
tempo2 = tempo*60
total = tempo2+km2
print('Considerando o tempo total de {} dias e os {} km rodados, o total a se pagar ficará em R${:.2f}' .format(tempo, km, total))
