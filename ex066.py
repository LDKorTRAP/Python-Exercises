num = cont = soma = 0
while num != 999:
    num = int(input('Insira um valor inteiro (999 para parar): '))
    if num == 999:
        break
    soma  += num
    cont += 1
print(f'Foram digitados {cont} números, cujo somatório é de {soma}')