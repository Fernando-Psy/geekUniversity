while True:
    try:
        kg = float(input('Quantos quilogramas meu rei/rainha: '))
        l = kg / 0.45 #formula de conversão
    except ValueError:
        print('Só serão aceitos valores númericos...')
    else:
        print(f'Valor lido: {kg}')
        print(f'Valor convertido para libras: {l:.2f}')
        break
