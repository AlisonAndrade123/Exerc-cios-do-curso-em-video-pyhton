#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

'''def fatorial(num):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


print(fatorial(5))
'''

def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(f' x ', end=' ')
            else:
                print(f' = ', end=' ')
        f *= c
    return f


print(fatorial(5, show=True))