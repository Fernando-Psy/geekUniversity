while True:
    try:
        p = float(input('Digite um comprimento de polegadas: '))
        c = p * 2.54 #formula de conversão
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Polegada lida:> {p}')
        print(f'convertida para centímetros: {c}')
        break
