valores = list()
while True:
    v = (int(input('Digite um valor: ')))
    if v not in valores:
        valores.append(v)
        print('Valor adicionada com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in' S':
            break
    if continuar in 'N':
        break
print('-='*30)
valores.sort()
print(f'Você digitou os valores {valores}')