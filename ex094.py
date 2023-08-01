tudo = dict()
galera = list()
mulheres = []
mediaI = 0
peoples = 0

while True:
    tudo.clear()
    tudo['Nome'] = str(input('\nNome: '))
    tudo['Idade'] = int(input('Idade: '))
    mediaI += tudo['Idade']
    tudo['Sexo'] = str(input('Sexo(M/F): '))
    if tudo['Sexo'] in 'Ff':
        mulheres.append(tudo['Nome'])
    peoples += 1
    galera.append(tudo.copy())

    resp = str(input('Deseja continuar? (S/N) '))
    if resp in 'Nn':
        break

print('=-='*15)

print(f'\nTotal de cadastros: {peoples} pessoas')
print(f'\nMédia das idades: {mediaI/2} anos')
print(f'\nMulheres cadastradas: {mulheres}')
print('\nPessoas acima da média:')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'\nNome: {p["Nome"]} Sexo: {p["Sexo"]} Idade: {p["Idade"]}', end='')
print()
