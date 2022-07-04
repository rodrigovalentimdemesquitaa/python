numero = int(input('\033[35mMe diga um número qualquer: \033[m'))
resultado = numero % 2
if resultado == 0:
    resultado = 'PAR'
else:
    resultado = 'IMPAR'
print('O \033[34m{}\033[m é um número \033[34m{}\033[m'.format(numero, resultado))

'''if resultado == 0:
    print('O {} é um número PAR '.format(numero, resultado))
else:
    print('O {} é um número IMPAR'.format(numero, resultado))'''