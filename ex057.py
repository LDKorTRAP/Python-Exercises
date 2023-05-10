sexo = str(input("Insira seu sexo (M/F): ")).strip().capitalize()[0]
while sexo not in 'FM':
     sexo = str(input("Insira uma opção válida (M/F): ")).strip().capitalize()
print("Sexo {} registrado com sucesso." .format(sexo))