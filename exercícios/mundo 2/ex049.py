num = int(input('Digite um número para saber sua tabuada: '))
print('-'*12)
for t in range(1, 10+1):
    print('{} x {:2} = {}'.format(num, t, num*t))
print('-'*12)
print('FIM DA TABUADA!')