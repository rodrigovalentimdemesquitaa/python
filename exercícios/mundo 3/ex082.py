valores = []
pares = []
impares = []
totpar = totimpar = 0
while True:
    valores.append(int(input('Digite um número: ')))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'S':
            break
    if resposta in 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=-'*30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')


