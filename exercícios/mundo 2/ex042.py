r1 = int(input('Primeiro seguimento: '))
r2 = int(input('Segundo seguimento: '))
r3 = int(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    pode = 'POREM FORMAR'
    if r1 == r2 == r3:
        tria = ' EQUILÁTERO!'
    elif r1 != r2 != r3 != r1:
        tria = ' ESCALENO!'
    else:
        tria = ' ISÓSCELES!'
else:
    pode = 'NÃO PODEM FORMAR'
    tria = '!'
print('Os seguimentos acima {} um triângulo{}'.format(pode, tria))
