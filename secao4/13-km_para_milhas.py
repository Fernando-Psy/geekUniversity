while True:
    try:
        km = float(input('Digite a distância em quilômetros: '))
        m = km / 1.61 #formula de conversão
    except ValueError:
        print('Apenas valores númericos serão aceitos')
    else:
        print(f'Km digitados: {km}')
        print(f'Mesmo valor em milhas: {m:.2f}')
        break
