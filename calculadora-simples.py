#interface
print('----CALCULADORA----')
print('Escolha uma operação')
print('Adição = +')
print('Subtração = -')
print('Multiplicação = *')
print('Divisão = /')

#dados

op = input('Que operação deseja utilizar?')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = float(input('Digite o primeiro valor:'))
    y = float(input('Digite o segundo valor:'))

#operações

if op == '+':
    res = x + y
    print('Voce escolheu a adição. Resultado:{} + {} = {}'.format(x, y, res))
elif op == '-':
    res = x - y
    print('Voce escolheu a subtração. Resultado:{} - {} = {}'.format(x, y, res))
elif op == '*':
    res = x * y
    print('Voce escolheu a multiplicação. Resultado:{} x {} = {}'.format(x, y, res))
elif op == '/':
    res = x / y
    print('Voce escolheu a divisão. Resultado:{} / {} = {}'.format(x, y, res))
else:
    print('Operação inválida.')
print('Programa encerrado.')