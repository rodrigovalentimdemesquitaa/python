peso = float(input('Qual é seu peso? (km) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    p = 'ABAIXO DO PESO!'
elif 18.5 < imc <= 25:
    p = 'PESO NORMAL!'
    print('Parabéns! ', end='')
elif 25 < imc <= 30:
    p = 'SOBREPESO!'
elif 30 < imc <= 40:
    p = 'OBESIDADE!'
else:
    p = 'OBESIDADE MÓRBIDA!'

print('Você está {}'.format(p))