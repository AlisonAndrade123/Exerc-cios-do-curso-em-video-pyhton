lanche = ('Hambúrquer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print(sorted(lanche))

print(lanche.index('Suco'))

print(lanche.count('Suco'))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5,1))

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa)
print(pessoa)