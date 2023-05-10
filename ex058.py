from random import randint
obj = randint(0, 10)
num = int(input('Pensei em um número de 0 a 10, tente advinhar: '))
cont = 1
if num == obj:
    print("Parabéns, o número era {} e você acerto em 1 tentativa." .format(obj))
while num != obj:
    cont = cont + 1
    num = int(input('Tente novamente: '))
if cont > 1:
    print("Parabéns, o número era {} e você acerto em {} tentativas." .format(obj, cont))
