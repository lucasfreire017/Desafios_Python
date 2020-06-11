# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro número 3
# Quais foram os números pares

val = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Valores Digitados: {val}\n')

print(f'O número nove foi digitado {val.count(9)} vezes')
if 3 in val:
    print(f'O número três foi digiitado primeiro na {val.index(3)+1}ª posição')
else:
    print(f'O número três não foi digitado')
print('Os números pares digitados foram: ', end='')

for n in val:
    if n % 2 == 0:
        print(n, end='')
