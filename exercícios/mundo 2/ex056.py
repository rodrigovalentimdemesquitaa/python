somaidade = mediaidade = maioridade = totmulher = 0
nomevelhor = ''
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    somaidade += idade
    mediaidade = somaidade / 4
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher += 1
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridade, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))

