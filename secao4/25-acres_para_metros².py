while True:
    try:
        a = float(input('Digite a quantidade de acres: '))
        m = a * 4048.58 #formula de conversão
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Valor lido: {a}')
        print(f'acres convertidos para metros quadrados: {m}')
        break
