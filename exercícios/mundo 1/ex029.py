velocidade =  float(input('Qual é velocidade atual do carro: '))
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}\033[m'.format(multa))
print('\033[34mTenha um bom dia! Dirija com segurança!\033[m')