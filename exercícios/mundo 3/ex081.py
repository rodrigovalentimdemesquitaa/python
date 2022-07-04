lista = []
elementos = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    elementos += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'S':
            break
    if resposta in 'N':
        break
print('=-'*30)
lista.sort(reverse=True)
print(f'Você digitou {elementos} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
