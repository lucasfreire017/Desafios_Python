n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2
if media < 5.0:
    print('Com a nota {} e {} a média é {} e o aluno está \033[1;32mREPROVADO\033[m'.format(n1, n2, media))
elif media <=6.9:
    print('Com a nota {} e {} a média é {} e o aluno está \033[1;33mRECUPERAÇÃO\033[m'.format(n1, n2, media))
else:
    print('Com a nota {} e {} a média é {} e o aluno está \033[1;34mAPROVADO\033[m'.format(n1, n2, media))
