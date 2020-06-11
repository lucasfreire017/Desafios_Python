aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))

if aluno['Média'] < 5:
    aluno['Situação'] = str('Reprovado')

elif 5 <= aluno['Média'] <7:
    aluno['Situação'] = str('Recuperação')

else: aluno['Situação'] = str('Aprovado')

print('=-'*30)

# Exibir valores das keys e values
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')