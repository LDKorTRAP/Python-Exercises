from datetime import date
print('\033[1;36mBEM VINDO AO ALISTAMENTO MILITAR DA MARINHA DE LEVIGNUS\033[m')
print('Eu sou a \033[35mAlmirante Lily\033[m, estarei lhe acompanhando neste processo')
ano = int(input('Primeiro, me diga qual o seu ano de nascimento: '))
atual = date.today().year
age = atual-ano
if age == 18:
    print('Muito bom, você está na idade certa do alistamento.')
elif age == 19:
    print('\033[1;31mVocê sabe que seu alistamento deveria ter sido feito a 1 ano atrás né? Sua chance de escapar acabou de cair pra zero, espertalhão do cacete.\033[m')
elif age > 19:
    print('\033[1;31mVocê sabe que seu alistamento deveria ter sido feito a {} ano atrás né? Sua chance de escapar acabou de cair pra zero, espertalhão do cacete.\033[m' .format(age-18))
    saldo = age - 18
    print('Seu alistamento deveria ter ocorrido em {}.' .format(atual-saldo))
else:
    print('\033[35mVeja bem meu querido, você não atingiu a idade necessária para ingressar na nossa corporação. Você ainda é como um bebê aos nossos olhos. Volte aqui dentro de {} anos, eu estarei exatamente aqui para te ajudar a entrar ^-^\033[m' .format(18-age))
    saldo = 18 - age
    print('Seu alistamento será em {}.' .format(atual+saldo))
