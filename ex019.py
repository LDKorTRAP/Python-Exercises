import random
aln1 = input('Primeiro aluno: ')
aln2 = input('Segundo aluno: ')
aln3 = input('Terceiro aluno: ')
aln4 = input('Quarto aluno: ')
lista = [aln1, aln2, aln3, aln4]
print('O aluno escolhido foi {}.' .format(random.choice(lista)))
