while True:
    try:
        angulo_graus = float(input('Digite o grau do ângulo: '))
        Pi = 3.14
        r = angulo_graus * Pi / 180 #formula de conversão
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'Valor lido: {angulo_graus}')
        print(f'Convertido para radianos: {r:.2f}')
        break
