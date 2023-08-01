resp = str('SIM')
lista = []

while resp != 'N':
    lista.append(int(input('Insira um novo valor: ')))
    resp = str(input('Deseja continuar? (S/N) ')).upper()

lista.sort(reverse=True)
print(f'Lista digitada: {lista}')

print(f'Total de número digitados: {len(lista)}')

if 5 in lista:
    print('O valor 5 foi digitado e inserido na lista')
else:
    print('O valor cinco não foi digitado e não está na lista')
