valores = list()

#Adição de valores na lista
for val in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {val}: ')))

#Análise de maior e menor valor na lista
maior = max(valores)
menor = min(valores)

#Análise das posições
pos_max = list()
pos_min = list()

for pos, v in enumerate(valores):
    if v == maior:
        pos_max.append(pos)

    if v == menor:
        pos_min.append(pos)

print('-'*37)
print(f"""Você digitou os seguintes valores: {valores}
O maior valor foi {maior} nas posições: {pos_max}
O menor valor foi {menor} nas posições: {pos_min}""")
