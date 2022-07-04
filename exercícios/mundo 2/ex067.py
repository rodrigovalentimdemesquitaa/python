while True:
    tabuada = int(input('Quer ver a tabuada de qual valor: '))
    print('-'*40)
    if tabuada < 0:
        break
    for t in range(1, 11):
        print(f'{tabuada} x {t:2} = {tabuada*t}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre')
