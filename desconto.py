p = float(input('Digite o preço do produto:'))
d = float(input('Digite o percentual de desconto(0-100)%:'))
des = p * (d / 100)  #Calculo do valor do desconto
res = p - des #Calculo do valor final

print('O preço do produto é {}. O Desconto é de {}%'.format(p, d))
print('O Valor do desconto é: {}. Valor final do produto: {}'.format(des, res))