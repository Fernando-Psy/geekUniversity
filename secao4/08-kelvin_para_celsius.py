while True:
    try:
        k = float(input('Digite a temperatura Kelvin por favor: '))
        c = k - 273.15 #formula de conversão
    except ValueError:
        print('Apenas valores númericos serão aceitos!')
    else:
        print(f'Temperatura em Kelvin: {k}')
        print(f'Mesma temperatura em Celsius: {c}')
        break
