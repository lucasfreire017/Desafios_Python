from Desafio_107 import moeda

valor = int(input('Digite o preço: R$'))

print(f'Aumentando {valor} em 10%, temos: R${moeda.aumento(valor)}')
print(f'Diminuindo em 13%, temos: R${moeda.diminuir(valor)}')
print(f'Dobrando o valor, temos: R${moeda.dobro(valor)}')
print(f'Dividindo pela metade, temos: R${moeda.metade(valor)}')

