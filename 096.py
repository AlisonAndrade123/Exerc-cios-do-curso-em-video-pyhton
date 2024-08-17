#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangula (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m².')

print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (M): '))
area(largura, comprimento)
