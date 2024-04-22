#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#À vista dinheiro/cheque: 10% de desconto 
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print(f'{" LOJA DO ALISON ":=^40}')

valor = float(input('Preço das compras: R$'))


print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('qual é a opção? '))

if opcao == 1:
    valor_desconto = valor - (valor / 100) * 10
    print(f'Sua compra de R$ {valor:.2f} vai custar R$ {valor_desconto:.2f} no final.')
elif opcao == 2:
    valor_desconto = valor - (valor / 100) * 5
    print(f'Sua compra de R$ {valor:.2f} vai custar R$ {valor_desconto:.2f} no final.')
elif opcao == 3:
    valor_parcelado = valor / 2
    print(f'Sua compra será parcelada em 2x de R${valor_parcelado:.2f}')
    print(f'Sua compra de R$ {valor:.2f} vai custar R$ {valor:.2f} no final.')
elif opcao == 4:
    quantas_parcelas = int(input('Quantas parcelas? '))
    valor_juros = valor + (valor / 100) * 20
    valor_parcelado = valor_juros / quantas_parcelas
    print(f'Sua compra será parcelada em {quantas_parcelas}x de R${valor_parcelado:.2f} COM JUROS')
    print(f'Sua compra de R$ {valor:.2f} vai custar R$ {valor_juros:.2f} no final.')
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')