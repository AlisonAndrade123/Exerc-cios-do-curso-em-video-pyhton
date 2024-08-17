'''
def traco():
    print('-' * 30)

traco()
print('CURSO EM VÍDEO'.center(30))
traco()
traco()
print('APRENDA PYTHON'.center(30))
traco()
traco()
print('ALISON A LENDA'.center(30))
'''
'''
def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)

mensagem('SISTEMA DE ALUNOS'.center(30))
'''
'''
def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

titulo('CURSO EM VÍDEO'.center(30))
titulo('APRENDA PYTHON'.center(30))
titulo('ALISON A LENDA'.center(30))
'''
'''
def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    print()

soma(4,5)
soma(8,9)
soma(2,1)
soma(b=4, a=5)
'''
'''
def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIM!')
        
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
'''
'''
def contador(*num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números')

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
'''
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7,2,5,0,4]
dobra(valores)
print(valores)
'''
''''
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5,2)
soma(2,9,4)
'''