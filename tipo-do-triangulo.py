#Pedindo o valor dos lados do triangulo
a = int(input('Digite o primeiro lado:'))
b = int(input('Digite o segundo lado:'))
c = int(input('Digite o terceiro lado:'))
#Validando os dados para saber se é um triangulo
if (a > 0) and (b > 0) and (c > 0):
    if (a + b > c) and (b + c > a) and (c + a > b):
    #Se for um triangulo o algoritmo continua para descobrir o tipo dele
        if (a != b) and (a != c) and (b != c):
            print('Esse é um triangulo escaleno')
        else:
            if (a == b and a == c and b == c):
                print('Esse é um triangulo equilátero')
            else:
                print('Esse é um triangulo isósceles')
    else:
        print('Ao menos um dos valores indicados não são válidos.')
else:
    print('Ao menos um dos valores indicados não são válidos.')
