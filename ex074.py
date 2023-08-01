import random
list = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
print(f'Valores sorteados: {list[0]} {list[1]} {list[2]} {list[3]} {list[4]}')
list.sort(reverse=False)
print(f'Menor número: {list[0]} \nMaior número: {list[4]}')