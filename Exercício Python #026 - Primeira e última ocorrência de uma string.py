frase = str(input('Digite uma frase: ').lower().strip())
print('-=-'*10)
print('A letra "A" aparece {} vezes na frase:'.format(frase.count('a')))
print('{}'.format(frase.replace('a','\033[1;32ma\033[m')))