dados = list()
alunos = cont = 0

while True:

    nome = str(input('\n\033[34mNome do aluno:\033[m '))
    n1 = float(input('\033[34mNota 1:\033[m '))
    n2 = float(input('\033[34mNota 2:\033[m '))
    media = (n1 + n2)/2
    dados.append([nome, [n1, n2], media])
    alunos += 1

    resp = str(input('\033[34mDeseja continuar? (S/N)\033[m '))
    if resp in 'Nn':
        break

print('\033[35m=-=\033[m'*15)
print(f'\033[1;34m{"No.":<4}{"Nome":<10}{"Média":>8}\033[m')

for i, a in enumerate(dados):
    print(f'\033[34m{i:<4}{a[0]:<10}{a[2]:>8.1f}\033[m')

print('\033[35m=-=\033[m'*15)

while True:
    al = int(input('\n\033[34mDe qual aluno deseja ver as notas? (69 para finalizar)\033[m '))
    if al == 69:
        print('\n\033[1;31mFinalizando!\033[m')
        break
    elif al <= len(dados) - 1:
        print(f'\n\033[35mAluno: {dados[al][0]} \nNotas: {dados[al][1]}\033[m')
    else:
        print('\n\033[1;31mInsira um aluno válido!\033[m')

