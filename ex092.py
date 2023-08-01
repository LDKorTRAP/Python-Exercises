import datetime
dados = {}
hoje = datetime.date.today().year

dados['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['Idade'] = hoje - ano
dados['CTPS'] = int(input('CTPS: (0 se não possui): '))

if dados['CTPS'] == 0:
    for c, i in dados.items():
        print(f'{c} tem valor {i}')

else:
    dados['Cotratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = int(dados['Cotratação'] + 35) - datetime.datetime.now().year
    print('+-+' * 15)

    for c, i in dados.items():
        print(f'{c} tem valor {i}')