frase = str(input('Digite uma frase: '))
splitada = frase.split()
juncao = ''.join(splitada).upper()
comprimento = len(juncao)
r1 = juncao[::-1]

if juncao == r1:
    print('A frase "{}" é um \033[1;32mPALÍMDROMO\033[m'.format(frase))
    print('''\n\033[36mComparação:\033[m
    {}
    {}'''.format(juncao, r1))
else:
    print('A frase "{}" não é \033[1;31mPALÍMDROMO\033[m'.format(frase))
    print('''\n\033[36mComparação:\033[m
    {}
    {}'''.format(juncao, r1))
