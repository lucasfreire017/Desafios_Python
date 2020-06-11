cores = {
    'azul':'\033[4;34m',
    'limpa':'\033[m',
}
dia = input('Dia =').strip()
mes = input('Mês =').strip()
ano = input('Ano =').strip()
print('-=-'*20)
print('Você nasceu no dia {1}{2}{3} de {4}{5}{6} de {7}{8}{9}. Correto?'.format(cores['azul'], cores['azul'], dia, cores['limpa'], cores['azul'], mes, cores['limpa'], cores['azul'], ano, cores['limpa'], cores['limpa']))
