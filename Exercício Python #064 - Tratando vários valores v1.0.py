num = soma = cont = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print('-=' * 40)
print('No total, foram \033[1;35m{}\033[m valores digitados.'.format(cont))
print('A soma de todos os valores é: \033[1;35m{}\033[m'.format(soma))
