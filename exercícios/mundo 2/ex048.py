qtd = soma = 0 # minha resposta
for c in range(1, 500+1):
    if c % 2 != 0:
        if c % 3 == 0:
            qtd += 1
            soma += c
print('A soma de todos os {} valores solicitados é {}'.format(qtd, soma))
#duas formas
qtd = soma = 0 # resposta do professor Guanabara
for c in range(1, 501, 2):
    if c % 3 == 0:
        qtd += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(qtd, soma))
