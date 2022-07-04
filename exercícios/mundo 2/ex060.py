#forma mais rapida de fazer
'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

#usando o while

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

#usando o for

'''n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
print('Calculando {}! = '.format(n), end='')
for factorial in range(n, 0, -1):
    f *= factorial
    print('{}'.format(factorial), end='')
    print(' x ' if factorial > 1 else ' = ', end='')
print(f)'''
