from datetime import date
totmaior = totmenor = 0
atual = date.today().year
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu: '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pesssoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
