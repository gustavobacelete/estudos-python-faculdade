#Algoritmo que calcula o total de pessoas no cinema, o dinheiro e a média do dinheiro arrecadado.



total = 0
dinheiro = 0
print('Programa iniciado, digite "calcular" para ter os dados calculados.')
while True:
    idade = input('Quantos anos você tem?')
    if idade == 'calcular':
        break
    #Transformando a variavel em numero já q não digitou sair
    idade = int(idade)
    #Total de pessoas, a cada idade adiciona uma pessoa
    total += 1
    if idade < 9:
        ingresso = 0
    else: 
        if idade > 21:
            #Valor do ingresso se for maior que 21 anos
            ingresso = 30
        else:
          #Se não for menor que 9 e nem maior que 21 o ingresso vai ser 15 reais
            ingresso = 15
#Sempre que um ingresso é adicionado, adiciona o valor no dinheiro
    dinheiro += ingresso
#Calculo do dinheiro pro total de pessoas presentes.
media = dinheiro / total

print('Total de pessoas no cinema: {}'.format(total))
print('Total de dinheiro arrecadado: R${}'.format(dinheiro))
print('Media do dinheiro arrecadado: R${}'.format(media))