#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h. Mostre uma mensagem dizendo que ele foi multado.A multa vai custar R$7,00 por cada Km acima do limite.#

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')