num = cont = soma = 0
while True:
    num = int(input('Digite um valor (\033[1;36m999\033[m = \033[1;31mSTOP\033[m): '))
    if num == 999:
        break
    cont += 1
    soma += num
print('-' * 50)
print(f'Você digitou \033[1;31m{cont}\033[m números e a soma entre eles é \033[1;36m{soma}\033[m')
