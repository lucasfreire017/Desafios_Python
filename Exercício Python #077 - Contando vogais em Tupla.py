Palavras = ('Acorrentada',
            'Olho',
            'Anteconstitucional',
            'Derrapagem',
            'Jogatina',
            'Namoro',
            'Python',
            'Aulas')

for c in range(0, len(Palavras)):
    a = Palavras[c].lower().count('a')
    e = Palavras[c].lower().count('e')
    i = Palavras[c].lower().count('i')
    o = Palavras[c].lower().count('o')
    u = Palavras[c].lower().count('u')

    print(f'A palavra \033[1m{Palavras[c].upper()}\033[m contem as vogais: \033[31m{"a" *a}\033[m \033[32m{"e"*e}\033[m \033[33m{"i"*i}\033[m \033[34m{"o"*o}\033[m \033[35m{"u"*u}\033[m')
