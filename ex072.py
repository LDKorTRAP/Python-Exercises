nums = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']

num = int(input('Digite um número inteiro de 0 a 20: '))

while num > 20 or num < 0:
    num = int(input('Insira um número válido, tente novamente: '))

print(f'\nO número digita foi {num}, que por extenso é {nums[num]}')
