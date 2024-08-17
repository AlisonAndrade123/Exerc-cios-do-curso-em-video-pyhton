#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#A)De 1 até 10, de 1 em 1
#B)De 10 até 0, de 2 em 2
#C)Uma contagem personalizada.

from time import sleep
def contador(i,f,p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        if f < i:
            cont = i
            while cont >= f:
                print(f'{cont}', end=' ', flush=True)
                sleep(0.5)
                cont -= p
            print('FIM')

contador(1,10,1)
contador(100,0,10)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input())
fim = int(input())
pas = int(input())
contador(ini,fim,pas)