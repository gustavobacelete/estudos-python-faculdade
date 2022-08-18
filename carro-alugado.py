dia = int(input('Por quantos dias o carro foi alugado?'))
km = int(input('Quantos KM foram percorridos?'))
final = dia * 60 + km * 0.15 #Calculo do aluguel do carro com base nos km rodados por ele
print('O carro custa R$60 por dia e mais R$0,15 por KM rodados com ele.')
print('O valor do aluguel do carro com base em seu uso cotidiano, de {} dias e {} KM rodados, custou:R$ {}'.format(dia, km, final))
print('Obrigado por utilizar nosso programa!\n Gustavo Menezes')