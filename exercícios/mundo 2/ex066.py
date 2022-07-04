valor = cont = soma = 0
while True:
    valor = int(input('Digite um valor (999 para parar) '))
    if valor == 999:
        break
    cont += 1
    soma += valor
print('A soma dos {} valores foi {}.'.format(cont, soma))
