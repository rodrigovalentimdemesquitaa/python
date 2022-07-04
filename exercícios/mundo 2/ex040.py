n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
if 7 > media >= 5:
    print('O aluno está RECUPERAÇÃO!')
elif media < 5:
    print('O aluno está em REPROVADO!')
elif media >= 7:
    print('O aluno está APROVADO!')