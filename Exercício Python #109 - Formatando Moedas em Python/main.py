from Desafio_109 import moeda

valor = float(input('Digite o preço: R$'))

print(f'Aumentando {moeda.moeda(valor)} em 10%, temos: {moeda.aumento(valor, 10, True)}')
print(f'Diminuindo {moeda.moeda(valor)} em 13%, temos: {moeda.diminuir(valor, 13, True)}')
print(f'Dobrando o valor, temos: {moeda.dobro(valor, True)}')
print(f'Dividindo pela metade, temos: {moeda.metade(valor, True)}')
