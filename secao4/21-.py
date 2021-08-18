while True:
    try:
        l = float(input('Digite o valor da massa em libras: '))
        k = l * 0.45
    except ValueError:
        print('Apenas valores númericos serão aceitos')
    else:
        print(f'Valor lido: {l}')
        print(f'Mesmo valor em quilogramas: {k}')
        break
