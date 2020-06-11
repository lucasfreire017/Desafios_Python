cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul-escuro':'\033[1;34m',
         'roxo':'\033[1;35m',
         'azul-claro':'\033[1;36m'}
z = input('Digite algo:')
print('\033[30m-=-'*13)
print('{}É alfabético:{}'.format(cores['branco'], cores['limpa']),z.isalpha())
print('{}É numérico:{}'.format(cores['vermelho'], cores['limpa']),z.isnumeric())
print('{}É alfanumérico:{}'.format(cores['verde'], cores['limpa']),z.isalnum())
print('{}É um número decimal:{}'.format(cores['amarelo'], cores['limpa']),z.isdecimal())
print('{}Tem apenas letras mínusculas:{}'.format(cores['azul-escuro'], cores['limpa']),z.islower())
print('{}É um título:{}'.format(cores['roxo'], cores['limpa']),z.istitle())
print('{}Tem só espaços:{}'.format(cores['azul-claro'], cores['limpa']),z.isspace())
