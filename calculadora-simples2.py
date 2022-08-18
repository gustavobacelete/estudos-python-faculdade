#Interface
print('----CALCULADORA----')
print('Escolha uma operação')
print('Adição = +')
print('Subtração = -')
print('Multiplicação = *')
print('Divisão = /')
print('Encerrar o programa = !')


      #Condição TRUE faz ela durar eternamente até que o break seja ativado
while True:
    #Dados
    op = input('Que operação deseja utilizar?')
    if op == '+' or op == '-' or op == '*' or op == '/':
      x = float(input('Digite o primeiro valor:'))
      y = float(input('Digite o segundo valor:'))    
    #operações  
    elif op == '+':
        res = x + y
        print('Voce escolheu a adição. Resultado:{} + {} = {}'.format(x, y, res))
        continue
    elif op == '-':
        res = x - y
        print('Voce escolheu a subtração. Resultado:{} - {} = {}'.format(x, y, res))
        continue
    elif op == '*':
        res = x * y
        print('Voce escolheu a multiplicação. Resultado:{} x {} = {}'.format(x, y, res))
        continue
    elif op == '/':
        res = x / y
        print('Voce escolheu a divisão. Resultado:{} / {} = {}'.format(x, y, res))
        continue
    elif op == '!':
      break
    else:
        print('Operação inválida.')
print('Programa encerrado.')
       