# A Condição S.N. é uma estrutura de decisão de Sim ou Não
val = list()

while True:
    n = int(input('Digite um valor:'))
    
    if n not in val:
        val.append(n)
        print('Valor adcionado com sucesso!')
    else:
        print('Valor já adcionado!')

    # Condição S.N.
    # Condição S.N. (Geral)
    resp = input('Deseja continuar [S/N]: ')[0].upper()
    if resp in 'Nn':
        break
    
print(f'Você digitou os seguintes valores: {val}')
val.sort()
print(f'Os valores em ordem crescente são: {val}')
