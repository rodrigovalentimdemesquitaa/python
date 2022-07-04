for p in range(1, 50+1):
    print('.', end='')
    if p % 2 == 0:
        mostre = p
        print(p, end=' ')
print('Acabou')

#duas formas de fazer a mesma coisa

for p in range(2, 51, 2):#dessa forma ocupa menos espaços.
    print('.', end='')  #observe os pontinhos.
    print(p, end=' ')
print('Acabou')