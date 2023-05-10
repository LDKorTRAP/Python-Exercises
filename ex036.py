print('\033[1;34mBem vindo ao banco NAV, o queridinho de Levignus\033[m')
print('\033[34mPara realizar um empréstimo, precisaremos de algumas informações antes.\033[m')
casa = int(input('Qual o valor da casa a ser comprada? '))
salário = float(input('Qual seu salário atual? '))
tempo1 = float(input('Em quantos anos pretende pagar? '))
tempo2 = tempo1*12
prestação = casa/tempo2
if prestação >= salário*.3:
    print('\033[1;31mSentimos muito, mas as prestações em um período de {:.0f} anos excedem as condições impostas, seu empréstimo será negado.\033[m' .format(tempo1))
else:
    print('\033[1;32mCom essas informações, podemos aprovar seu empréstimo para parcelas de R$ {:.2f}, a serem pagas em um total de {:.0f} meses. Parabéns.\033[m' .format(prestação, tempo2))
