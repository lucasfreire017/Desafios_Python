# Abaixo de 18.5: Abaixo do peso / amarelo 33
# Entre 18.5 e 25: Peso ideal / verde 32
# 25 até 30: Sobrepeso / amarelo 33
# 30 até 40: Obesidade / roxo 35
# Acima de 40: Obesidade mórbita / vermelho 31
cores = {'limpa':'\033[m',
         'azul':'\033[1;36m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'roxo':'\033[1;35m'
}
peso = float(input('Qual é seu peso em Kg? '))
altura = float(input('Qual é sua altura em m? '))
IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('-=' * 20)
    print('Seu IMC é de {}{:.1f}{}.'.format(cores['azul'], IMC, cores['limpa']))
    print('CUIDADO! Você está {}ABAIXO DO PESO{}.'.format(cores['amarelo'], cores['limpa']))

elif 18.5 <= IMC < 25:
    print('-=' * 20)
    print('Seu IMC é de {}{:.1f}{}.'.format(cores['azul'], IMC, cores['limpa']))
    print('PARABÉNS, Você está no {}PESO IDEAL{}.'.format(cores['verde'], cores['limpa']))

elif 25 <= IMC < 30:
    print('-=' * 20)
    print('Seu IMC é de {}{:.1f}{}.'.format(cores['azul'], IMC, cores['limpa']))
    print('ATENÇÃO! Você está com {}SOBREPESO{}.'.format(cores['amarelo'], cores['limpa']))

elif 30 <= IMC < 40:
    print('-=' * 20)
    print('Seu IMC é de {}{:.1f}{}.'.format(cores['azul'], IMC, cores['limpa']))
    print('ATENÇÃO! Você está com {}OBESIDADE{}.'.format(cores['roxo'], cores['limpa']))

else:
    print('-=' * 20)
    print('Seu IMC é de {}{:.1f}{}.'.format(cores['azul'], IMC, cores['limpa']))
    print('{}CUIDADO!{} Você está com {}OBESIDADE MÓRBITA{}.'.format(cores['vermelho'], cores['limpa'], cores['vermelho'], cores['limpa']))
