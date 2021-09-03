while True:
    try:
        m = float(input('Digite sua distância em milhas: '))
        k = 1.61 * m #formula de conversão
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Valor em milhas: {m}')
        print(f'Mesmo valor em quilômetros: {k}')
