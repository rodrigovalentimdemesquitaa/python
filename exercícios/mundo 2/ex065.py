#estudar
resp = 'S'
soma = qtd = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media = soma / qtd
print('Você digitou {} números e a média foi {}'.format(qtd, soma))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
