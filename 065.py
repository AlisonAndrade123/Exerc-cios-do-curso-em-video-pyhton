#Crie um programa que leia vários números inteiros pelo teclado. No final sa execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = cont = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')
print('Acabou')