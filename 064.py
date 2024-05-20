#Crie um programa que leia vários números inteiros pelo teclado o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

#num = cont = soma = 0

num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += num
    if num == 999:
        cont -= 1
        soma -= 999
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
print('Acabou')