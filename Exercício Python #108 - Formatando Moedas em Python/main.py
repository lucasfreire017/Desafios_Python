from Desafio_108 import moeda

valor = int(input('Digite o preço: R$'))

print(f'Aumentando em 10%, temos: {moeda.moeda(moeda.aumento(valor))}')
print(f'Diminuindo em 13%, temos: {moeda.moeda(moeda.diminuir(valor))}')
print(f'Dobrando o valor, temos: {moeda.moeda(moeda.dobro(valor))}')
print(f'Dividindo pela metade, temos: {moeda.moeda(moeda.metade(valor))}')

