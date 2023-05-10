maior = 0
menor = 0
média = 0
contador = 0
for p in range(1,5):
    print('---- {} Pessoa ----' .format(p))
    nome = str(input('\033[34mNome:\033[m '))
    idade = int(input('\033[35mIdade:\033[m '))
    sexo = str(input('\033[36mSexo(H/M):\033[m ')).upper()
    média = média + idade
    if sexo == 'M':
        if idade < 20:
            contador += 1
    if sexo == 'H':
        if p == 1:
            maior = idade
            menor = idade
            velho = nome
        else:
            if idade > maior:
                maior = idade
                velho = nome
            if idade < menor:
                menor = idade
print('------------------')
print('\033[35mA média das idades é {}.\033[m' .format(média/4))
print('\033[33m{} mulheres tem menos de 20 anos\033[m' .format(contador))
print('\033[31mO homem mais velho tem {} anos e seu nome é {}.\033[m' .format(maior, velho))
