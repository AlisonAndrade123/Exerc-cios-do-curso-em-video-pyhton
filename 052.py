#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
divisivel = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        divisivel += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {divisivel} vezes')
if divisivel == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')