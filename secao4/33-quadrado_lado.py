while True:
    try:
        l = int(input('Lado do quadrado: '))
        a = l*l # formula para calcular o lado do quadrado
    except ValueError:
        print('Apenas valores inteiros serão aceitos...')
    else:
        print(f'A área do quadrado é: {a}')
        break

