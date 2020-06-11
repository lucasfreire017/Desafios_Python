numero = int(input('Digite um número:'))
v = numero % 2
if v == 0:
  print('O número é {}\033[31m PAR!'.format(numero))
else:
  print('O número é {}\033[35m IMPAR!'.format(numero))