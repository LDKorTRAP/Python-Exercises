aluno = dict()

print('\033[35mColégio Naval Levginus\033[m')

aluno['nome'] = str(input('\033[31mAluno:\033[m '))
aluno['media'] = float(input('\033[31mMédia final:\033[m '))

if aluno['media'] >= 7:
    aluno['situ'] = str('Aprovado')

elif aluno['media'] < 7 and aluno['media'] >= 5:
    aluno['situ'] = str('de Recuperação')

else:
    aluno['situ'] = str('Reprovado')

print('\033[35m---- Dados Finais ----\033[m')
print(f'\n\033[31mNome:\033[m \033[35m{aluno["nome"]}\033[m \n\033[31mMédia Final:\033[m \033[35m{aluno["media"]}\033[m \n\033[31mSituação escolar:\033[m \033[35m{aluno["situ"]}\033[m')
