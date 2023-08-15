from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade < 18:
        print(f'Com atualmente {idade}: VOTO NEGADO')
    elif idade >= 18 and idade < 70:
        print(f'Com atualmente {idade}: VOTO OBRIGATÓRIO')
    else:
        print(f'Com atualmente {idade}: VOTO OPCIONAL')


ano = int(input('Qual o seu ano de nascimento? '))
voto(ano)
