valor = int(input('Digte um valor:')) #Digite o valor que deseja fazer a contagem de cedulas
while True:
    if valor >= 100: #Cedulas de 100
        cedulas100 = valor // 100
        valor -= cedulas100 * 100
        print('Cedulas de 100: {}'.format(cedulas100))
        if not valor:
            break

    if valor >= 50: #Cedulas de 50
        cedulas50 = valor // 50
        valor -= cedulas50 * 50
        print('Cedulas de 50: {}'.format(cedulas50))
        if not valor:
            break
    if valor >= 20: #Cedulas de 20
        cedulas20 = valor // 20
        valor -= cedulas20 * 20
        print('Cedulas de 20: {}'.format(cedulas20))
        if not valor:
            break
    if valor >= 10: #Cedulas de 10
        cedulas10 = valor // 10
        valor -= cedulas10 * 10
        print('Cedulas de 10: {}'.format(cedulas10))
        if not valor:
            break
    if valor >= 5: #Cedulas de 5
        cedulas5 = valor // 5
        valor -= cedulas5 * 5
        print('Cedulas de 5: {}'.format(cedulas5))
        if not valor:
            break
    if valor: #Cedulas de 1
        cedulas1 = valor
        print('Cedulas de 1: {}'.format(cedulas1))
        break