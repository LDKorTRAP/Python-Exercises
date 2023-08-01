option = str('S')
contMasc = cont20 = cont18 = 0

while option != 'N':
    sexo = str(input('Sexo (M/F): ')).upper()
    idade = int(input('Idade: '))
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        contMasc += 1;
    if sexo == 'F':
        if idade < 20:
            cont20 += 1
    option = str(input('Deseja continuar?(S/N) ')).upper()
    if option == 'N':
        break
print(f'\nPessoas com mais de 18: {cont18} \nHomens registrados: {contMasc} \nMulheres com menos de 20: {cont20}')
