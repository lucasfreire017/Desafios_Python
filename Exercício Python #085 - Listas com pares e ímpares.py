# Digitar sete valores / Uma lista / separar impares e pares / exibir em ordem crescente

main = list(),list()
number = 0
x = 0
for c in range(0, 7):
    number = int(input(f'Digite o {c+1}° valor: '))

    if number % 2 == 0:
        main[0].append(number)
    else:
        main[1].append(number)

print('-=' * 20)

main[0].sort()
main[1].sort()

print(f'Valores pares: {main[0]}')
print(f'Valores impares: {main[1]}')
