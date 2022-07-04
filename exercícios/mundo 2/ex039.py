from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} em {}.'.format(ano, idade, atual))
if idade < 18:
    fidade = 18 - idade
    fano = atual + fidade
    print('Ainda faltam {} anos para o alistamento'.format(fidade))
    print('Seu alistamento será em {}'.format(fano))
elif idade > 18:
    fidade = idade - 18
    print('Você já deveria ter se alistado há {} anos '.format(fidade))
    fano = atual - fidade
    print('Seu alistamento foi em {}'.format(fano))
else:
    print('Você tem que ser alistar IMEDIATAMENTE!')