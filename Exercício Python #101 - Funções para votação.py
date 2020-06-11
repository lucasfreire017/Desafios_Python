def voto(ano_nasc):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    if idade < 18:
        voto = "NÃO VOTA"

    if idade >= 18 and idade < 65:
        voto = "VOTO OBRIGATÓRIO"

    if idade >= 65:
        voto = "VOTO OPCIONAL"


    print(f'Com {idade} anos: {voto}')


print('-='*20)
ano_nasc = int(input('Em que ano você nasceu? '))
voto(ano_nasc)