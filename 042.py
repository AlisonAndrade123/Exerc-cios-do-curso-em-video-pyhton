#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo, Equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Os segmentos acima PODEM FORMAR um triângulo, Isósceles!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Os segmentos acima PODEM FORMAR um triângulo, Escaleno!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')