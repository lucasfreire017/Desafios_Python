a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
c = int(input('Digite o terceiro valor:'))
maior = a
menor = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
