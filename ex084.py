import time
dados = list()
princ = list()
maisP = list()
menosP = list()
map = mep = 0
cont = 0

print('\033[1;35mCandidatas à modelo\033[m')
while True:
    dados.append(str(input('\n\033[34mNome:\033[m ')))
    dados.append(float(input('\033[34mPeso:\033[m ')))

    if len(princ) == 0:
        map = mep = dados[1]
    else:
        if dados[1] > map:
            map = dados[1]
        if dados[1] < mep:
            mep = dados[1]

    princ.append(dados[:])
    dados.clear()

    option = str(input('\033[1;35mDeseja continuar? (S/N)\033[m '))
    if option in 'Nn':
        break
    else:
        dados.clear()

print('\033[1;35mPROCESSANDO DADOS\033[m', end='')
for c in range(0,3):
    print('\033[35m.\033[m', end='')
    time.sleep(1)

print(f'\n\033[1;34mTotal de pessoas registradas:\033[m \033[35m{len(princ)}\033[m')
print(f'\033[1;34mMaior peso:\033[m \033[35m{map} kg.\033[m \033[34mPessoas registradas:\033[m ', end='')

for p in princ:
    if p[1] == map:
        print(f'\033[35m[{p[0].lower().capitalize()}]\033[m ', end='')

print(f'\n\033[1;34mMenor peso:\033[m \033[35m{mep} kg.\033[m \033[34mPessoas registradas:\033[m ', end='')

for p in princ:
    if p[1] == mep:
        print(f'\033[35m[{p[0].lower().capitalize()}]\033[m ', end='')