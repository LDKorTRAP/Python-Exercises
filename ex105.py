resp = dict()

def nota(*n, sit = False):
    """
    N -> Conjunto de valores dados como notas.
    SIT -> String referente a situação acadêmica.
    MENOR -> Menor valor registrado dentro do conjunto N.
    MAIOR -> Maior valor registrado dentro do conjunto N.
    TOTAL -> Total de valores do conjunto N.
    MÉDIA -> Valor referente a divisão entre o somatório dos valores de N e seu número de elementos.
    """
    resp['total'] = len(n)
    resp['maior'] = max(n)
    resp['menor'] = min(n)
    resp['média'] = sum(n)/len(n)
    if sit:
        if resp['média'] >= 7:
            resp['situação'] = 'Boa'
        elif resp['média'] >= 5:
            resp['situação'] = 'Mediana'
        else:
            resp['situação'] = 'Terrível'
    return resp


n = nota(2, 5, 4, sit=True)
print(resp)
