matriz = list()
x = y = 0
for c in range(0, 9):
    matriz.append(int(input(f'Digite um valor para a posição [{x}, {y}]: ')))
    y += 1

    if y == 3:
        x += 1
        y = 0

print('-='*30)
print(f'[ {matriz[0]:^5} ] [ {matriz[1]:^5} ] [ {matriz[2]:^5} ]')
print(f'[ {matriz[3]:^5} ] [ {matriz[4]:^5} ] [ {matriz[5]:^5} ]')
print(f'[ {matriz[6]:^5} ] [ {matriz[7]:^5} ] [ {matriz[8]:^5} ]')