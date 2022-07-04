print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('='*40)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for t in range(primeiro, decimo+1, razão):
    print(t, end=' - ')
print('ACABOU')