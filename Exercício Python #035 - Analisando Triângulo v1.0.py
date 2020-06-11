cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[33m',
         'azul':'\033[36m'}

print('-='*20)
print('{}Analisador de Triangulos{}'.format(cores['amarelo'], cores['limpa'] ))
print('-='*20)
r1 = float(input('{}Primeiro Seguimento:{}'.format(cores['azul'], cores['limpa'])))
r2 = float(input('{}Segundo Seguimento:{}'.format(cores['azul'], cores['limpa'])))
r3 = float(input('{}Terceiro Segumento:{}'.format(cores['azul'], cores['limpa'])))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('Os seguimentos acima {}PODEM FORMAR{} um triângulo.'.format(cores['verde'], cores['limpa']))
else:
    print('Os seguimentos acima {}NÃO PODEM{} formar um triângulo.'.format(cores['vermelho'], cores['limpa']))
