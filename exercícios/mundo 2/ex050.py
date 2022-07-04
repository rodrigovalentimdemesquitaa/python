qtd = soma = 0
for num in range(1, 7):
    numero = int(input('Digite {}º valor: '.format(num)))
    if numero % 2 == 0:
        soma += numero
        qtd += 1
print('Você informou {} números PARES e a soma foi {}'.format(qtd, soma))
