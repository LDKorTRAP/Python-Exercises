nums = []
pares = []
impar = []
cont = 0

while True:
    nums.append(int(input('Insira um novo valor: ')))
    if nums[cont] % 2 == 0:
        pares.append(nums[cont])
    else:
        impar.append(nums[cont])
    cont += 1
    resp = str(input('Deseja continuar? (S/N) ')).upper()
    if resp in 'Nn':
        break

nums.sort()
pares.sort()
impar.sort()

print(f'listas geradas \nNúmeros digitados: {nums} \nPares: {pares} \nÍmpares: {impar}')
