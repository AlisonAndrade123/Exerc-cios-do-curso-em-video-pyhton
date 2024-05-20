#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorialde {n} é {f}.')'''

'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end = '')
while c > 0:
    print(f'{c}', end = ' ')
    print('x ' if c > 1 else '=', end = '')
    f *= c
    c -= 1
print(f' {f}.')'''


n = int(input('Digite um número para calcular seu Fatorial: '))
f = 1
print(f'Calculando {n}! = ', end = '')
for c in range(n, 0, -1):
    print(f'{c}', end = ' ')
    f *= c
    if c > 1:
        print('x ', end = '')
    else:
        print('=', end = '')
print(f' {f}.')