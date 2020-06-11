from random import shuffle

a = str(input('Primeiro aluno(a):'))
b = str(input('Segundo aluno(a):'))
c = str(input('Terceiro aluno:'))
d = str(input('Quarto aluno(a):'))
lista = [a, b, c, d]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
