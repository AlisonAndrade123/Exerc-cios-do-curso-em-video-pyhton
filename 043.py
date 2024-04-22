#Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: ABAIXO DO PESO
#ENTRE 18.5 e 25: PESO IDEAL
#25 até 30: SOBREPESO
#30 até 40: OBESIDADE
#Acima de 40: OBESIDADE MÓRBIDA

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

IMC = peso / (altura **2)

print(f'O IMC dessa pessoa é de {IMC:.1f}')

if IMC < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= IMC < 25:
    print('Você está no PESO IDEAL!')
elif 25 <= IMC < 30:
    print('Você está com SOBREPESO!')
elif 30 <= IMC < 40:
    print('Você está com OBESIDADE!') 
else:
    print('Você está com OBESIDADE MÓRBIDA!')