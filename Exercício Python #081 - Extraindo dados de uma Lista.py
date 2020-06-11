# Número de elementos
# Valores em ordem decrescente
# Se o valor 5 faz parte da lista

List = list()

while True:
    # Adição de valores a lista
    List.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
    if resp not in 'Ss':
        break
    

print('-+' * 20)  
print(f'A lista contem {len(List)} elementos')

List.sort(reverse=True)
print(f'Os valores da lista em ordem decrescente: {List}')
    
if 5 in List:
    print('O valor 5 foi encontrado na lista')
else:
    print('O valor 5 não foi encontrado na lista')
    