print('='*12, end='')
print(' LOJAS GUANABARA ', end='')
print('='*12)
valor = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual opção? '))
if opção == 1:
    jd = valor - (valor * 10/100)
elif opção == 2:
    jd = valor - (valor * 5/100)
elif opção == 3:
    print('Sua compra será parcelada em 2x de R${} SEM JUROS'.format(valor / 2))
    jd = valor
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    jd = valor + (valor * 20 / 100)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, jd / parcelas))
else:
    jd = valor
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!')
print('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(valor, jd ))
