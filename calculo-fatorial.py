def valida(pergunta, min, max):
    x = int(input(pergunta)) 
    while x < min or x > max: #Se x for menor que minimo ou maior que maximo
        x = int(input(pergunta))#Ele vai repetir a pergunta até dar um valor positivo entre os intervalos pedidos
    return x #Retorna o X e acaba a repetição


def fatorial(num):
    """
    Calcula a fatorial
    """
    fat = 1
    if num == 0:
        return fat #Se num for igual a 0, retorna para o fat que vale 1, se não for, continua para a linha de baixo
    for i in range(1, num+1, 1): #Faz o calculo da fatorial, começando em 1 e terminando no numero + 1 pra dar o valor certinho pedido.
        fat *= i  # fat = fat * i
    return fat #Retorna o valor de fat já calculado pra função


# Programa Principal
x = valida('Digite um valor para calcular a fatorial:', 0, 99999)   
print('{}! = {}'.format(x, fatorial(x)))# Função fatorial com o parametro X dentro dela, que ai calcula a fatorial de X