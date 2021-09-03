while True:
    try:
        j = float(input('Qauntidade de jardas: '))
        m = 0.91 * j #formula de conversão
    except ValueError:
        print('Apenas valores númericos serão aceios...')
    else:
        print(f'Valor lido: {j}')
        print(f'Valor convertido para metros: {m}')
        break
