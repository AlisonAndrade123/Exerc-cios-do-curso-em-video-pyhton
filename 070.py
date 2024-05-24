#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#C) Qual é o nome do produto mais barato.

soma = mais_de_1000 = mais_barato = cont = 0
barato_produto = ''
print('-' * 30)
print(f'{'LOJA SUPER BARATÃO': ^30}')
print('-' * 30)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    if preco > 1000:
        mais_de_1000 += 1
    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        barato_produto = produto
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continua not in ['S', 'N']:
        continua = input('Por favor, escolha entre sim (S) ou não (N): ').strip().upper()[0]
    if continua == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {mais_de_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato_produto} que custa {mais_barato:.2f}')