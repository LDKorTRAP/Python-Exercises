print('\033[1;35m{} Conselho de classe {}\033[m' .format('='*6, '='*6))
n1 = float(input('Qual a primeira nota do aluno: '))
n2 = float(input('Qual a segunda nota do aluno: '))
média = (n1+n2)/2
if média < 5:
    print('\033[31mOlha, com uma média de {}, ele tá reprovado direto sem direito a recuperação.\033[m' .format(média))
elif 7 > média >= 5:
    print('\033[33mCom uma média de {}, esse aluno está apenas de recuperação.\033[m' .format(média))
else:
    print('\033[35mEsse aluno está aprovado com uma média de {}, e passou de ano.\033[m' .format(média))
