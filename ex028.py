import random

n1 = random.randint(10,20)
print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
      "To pensando em um número, entre 10 e 20.\n"
      "-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
n2 = float(input('Qual sería esse número? '))
if n2 == n1:
    print('Você ganhou!')
    print('Parabéns, baby, você acertou! Sua recompensa vai ser um blowjob bem rápido.')
else:
    print('haha, eu ganhei. O número era {}, e não {:.0f}.' .format(n1, n2))
    print('Que pena, você errou e não vai ganhar o grande prêmio.')
