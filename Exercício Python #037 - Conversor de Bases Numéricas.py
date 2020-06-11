num = int(input('Digite qualquer número:'))
opcao = {'binario':bin(num), 'octal':oct(num), 'hexadecimal':hex(num)}
print("""-=-=-=-=-=-=-=-=-
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
-=-=-=-=-=-=-=-=-""")
escolha = int(input('Qual das opçoes deseja converter seu número? '))
if escolha == 1:
    print(opcao['binario'][2:])
elif escolha == 2:
    print(opcao['octal'][2:])
elif escolha == 3:
    print(opcao['hexadecimal'][2:])
else:
    print('\033[1;31mOPÇÃO INVÁLIDA')
