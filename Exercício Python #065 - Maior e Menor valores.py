num = cont = maior = menor = soma = média = 0
resp = str('s')
while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    média = soma / cont
print(f'Você digitou {cont} valores e a média entre eles é \033[1;32m{média}\033[m')
print(f'O maior valor foi \033[1;35m{maior}\033[m')
print(f'O menor valor foi \033[1;35m{menor}\033[m')
