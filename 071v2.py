print('=' * 30)
print(f'{'BANCO CEV': ^30}')
print('=' * 30)
valor = int(input('Que valor voçe quer sacar? R$'))
quantidade_notas_50 = valor // 50
valor %= 50
quantidade_notas_20 = valor // 20
valor %= 20
quantidade_notas_10 = valor // 10
valor %= 10
quantidade_notas_1 = valor
print(f'Total de {quantidade_notas_50} cédulas de R$50')
print(f'Total de {quantidade_notas_20} cédulas de R$20')
print(f'Total de {quantidade_notas_10} cédulas de R$10')
print(f'Total de {quantidade_notas_1} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')