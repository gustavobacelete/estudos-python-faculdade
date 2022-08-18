kwh = float(input('Quantos kWh?')) #Pede os kWh gastos pela instalação
tipo = (input('Que tipo de instalação? (C, R, I')) #Pede o tipo da instalação
# C - comércios
# R - residencias
# I - industrias

if tipo == 'R':
    if kwh <= 500: #Se for maior que 500 kwh irá pagar R$0.50 a cada kwh
        preco = 0.4 
    else:
        preco = 0.5
elif tipo == 'C':
    if kwh <= 1000: #Se for maior que 1000 kwh irá pagar R$0.65 a cada kwh
        preco = 0.55
    else:
        preco = 0.65
elif tipo == 'I':
    if kwh <= 5000: #Se for maior que 5000 kwh irá pagar R$0.80 a cada kwh
        preco = 0.7
    else:
        preco = 0.8
else:
    print('Tipo invalido') #Erro se digitar uma instalação inexistente

print('Valor a pagar:{}'.format(kwh * preco))
