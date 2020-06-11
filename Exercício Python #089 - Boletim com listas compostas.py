# Lista temporária
temp = list()
# Lista principal
alunos = list()

while True:
    
    # Adição de valores na lista temporária
    temp.append(input('Digite o nome do aluno(a): '))
    temp.append(float(input('Digite a 1° nota: ')))
    temp.append(float(input('Digite a 2° nota: ',)))
    
    alunos.append(temp[:])
    temp.clear()
    
    resp = input('\nDeseja continuar? [S/N]: ')[0]
    print('')
    
    if resp not in 'Ss':
        break

print('=-'*30)

# Criação do boletim
print(f'{"Id":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for i, c in enumerate(alunos):
    print(f'{i:<4}{c[0]:<10}{(c[1]+c[2])/2:>8.1f}')   

while True:
    
    while True:  
        perg = int(input('\nDeseja ver a nota de qual aluno? (999 interrompe): '))

        # Caso o valor digitado seja incorreto
        if perg > (len(alunos) - 1) and  perg != 999: 
            print('Valor Incorreto, Tente Novamente\n')       
        else:
            break

    if perg == 999:
        break

    print('-=' *20)
    print(f'As notas de {alunos[perg][0]} são: {alunos[perg][1:]}')

print('\n<<<< PROGRAMA FINALIZADO >>>>')
