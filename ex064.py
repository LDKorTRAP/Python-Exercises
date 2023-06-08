import random
num = int(input('\033[4:32mDigite um número inteiro (999 para finalizar):\033[m '))
soma = 0
cont = 0
cores = ['\033[4:34m', '\033[4:35m', '\033[4:36m', '\033[4:37m']
while(num != 999):
    cor = random.choice(cores)
    soma += num
    cont += 1
    num = int(input("\n{} Digite outro número inteiro (999 para finalizar):\033[m " .format(cor)))
print('\nForam digitados {} números, sendo o somátório deles igual a {}\n' .format(cont, soma))
