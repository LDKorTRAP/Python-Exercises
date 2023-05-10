from datetime import date
print('\033[1;97m{} A Confederação está em busca em jovens talentos para todos os esportes, venha representar a ilha Mind! {}\033[m' .format('='*4, '='*4))
ano = int(input('\033[97mDigite aqui seu ano de nascimento:\033[m '))
idade = date.today().year - ano
if idade <= 9:
    print('\033[32mBem vindo(a) a categoria MIRIM!\033[m')
elif idade <= 14:
    print('\033[33mBem vindo(a) a categoria INFANTIL!\033[m')
elif idade <= 19:
    print('\033[34mBem vindo(a) a categoria JÚNIOR!\033[m')
elif idade <= 25:
    print('\033[35mBem vindo(a) a categoria SÊNIOR!\033[m')
else:
    print('\033[36mBem vindo(a) a categoria MASTER!\033[m')
