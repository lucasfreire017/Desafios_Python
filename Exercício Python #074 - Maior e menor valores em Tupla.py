from random import randint

#Sorteiamento de valores
num = (randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10),
       randint(0, 10))

print(f'Os valores sorteados foram: {num[0]} {num[1]} {num[2]} {num[3]} {num[4]}\n')
print(f'O maior número é: {max(num)}')
print(f'O menor valor é: {min(num)}')
