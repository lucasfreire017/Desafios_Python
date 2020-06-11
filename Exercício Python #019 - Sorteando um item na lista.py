from random import choice
a = str(input('Digite o nome do primiro aluno(a):'))
b = str(input('Digite o nome do segundo aluno(a):'))
c = str(input('Digite o nome do terceiro aluno(a):'))
d = str(input('Digite o nome do quarto aluno(a):'))
lista = [a, b, c, d]
r = choice(lista)
print('O aluno(a) escolhido foi: {}'.format(r))
