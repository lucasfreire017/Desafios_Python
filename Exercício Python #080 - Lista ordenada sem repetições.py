val = list()

for c in range(0,5):
    x = int(input('Digite um valor: '))

    if c == 0 or x > val[-1]:
        val.append(x)
    else:
        pos = 0
        while pos < len(val):
            if x <= val[pos]:
                val.insert(pos, x)
                break
            pos += 1

print('-=' * 20)
print(f'Os valores digitados em ordem crescente foram: {val}')