while True:
    try:
        n = int(input('Digite um valor: '))  
    except ValueError:
        print('Apenas números inteiros serão aceitos')
    else:
        print(f'Número digitado: {n}')
        break
