# Crie uma lista e adcione valores nela
# Separe os valores impares e adcione em uma lista
# Separe os valores pares e adcione em uma lista

lista = list()
pares = list()
impares = list()

while True:
    # Adição de valores na lista principal
    lista.append(int(input('Digite algum valor: ')))

    # Adção de valores pares da lista principal
    if lista[-1] % 2 == 0:
        pares.append(lista[-1])

    # Adção de valores impares da lista principal
    if lista[-1] % 2 == 1:
        impares.append(lista[-1])

    # Estrutura de decisão Sim ou Não
    resp = str(input('Deseja continuar: [S/N]: '))
    if resp not in 'Ss':
        break

print('-='*30)
print(f'\033[31mTodos valores digitados:\033[m {lista} \n')
print(f'\033[32mTodos valores pares:\033[m {pares} \n')
print(f'\033[33mTodos valores impares:\033[m {impares} \n')
