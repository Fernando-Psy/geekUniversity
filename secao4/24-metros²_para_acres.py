while True:
    try:
        m = float(input('Metros quadrados(m²): '))
        a = m * 0.000247 #formula de conversão
    except ValueError:
        print('Apenas valores númericos serão aceitos')
    else:
        print(f'Valor lido: {m}')
        print(f'Metros cúbicos convertidos para acres: {a}')
