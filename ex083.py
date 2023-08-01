expression = str(input('Digite a expressão: '))
pilha = []
for simb in expression:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\033[1;35mExpressão válida\033[m')
else:
    print('\033[1;31mExpressão inválida\033[m')
