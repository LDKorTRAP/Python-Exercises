num = int(input("Insira quantos números da sequência devem aparecer: "))
cont = 0;
t1 = 0
t2 = 1
print("0 —> 1 —> ", end='')
if num > 2:
    while(cont <= num):
        cont += 1
        t3 = t1 + t2
        print("{} —> " .format(t3), end='')
        t1 = t2
        t2 = t3
print("FIM", end='')
