#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='') 
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')


'''from random import sample

# Gera uma lista com cinco números inteiros aleatórios entre 1 e 10, sem repetição
numeros = sample(range(1, 11), 5)

# Imprime os valores da lista
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')

# Inicializa o maior e o menor valor com o primeiro número da lista
maior_valor = numeros[0]
menor_valor = numeros[0]

# Itera sobre os números para encontrar o maior e o menor valor
for n in numeros:
    if n > maior_valor:
        maior_valor = n
    if n < menor_valor:
        menor_valor = n

# Imprime o maior e o menor valor
print(f'\nO maior valor sorteado foi: {maior_valor}')
print(f'O menor valor sorteado foi: {menor_valor}')'''
