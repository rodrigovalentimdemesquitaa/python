graus = float(input('Informe a temperatura em ºC: '))
#fan = graus * 1.8 + 32
fan = graus * 9/8 + 32
print('A temperatura de {}ºC corresponde a {}ºF'.format(graus, fan))