def lin():
    print('\033[35m-\033[m'*len(txt[pos]))

def escreva(txt):
        lin()
        print(f'\033[34m{txt[pos]}\033[m')
        lin()

pos = 0
txt = ['Curintias', 'Fofuria', 'Impe']
for c in range(0, len(txt)):
      escreva(txt)
      pos += 1