while True:
    try:
        altura = float(input('Digite a altura do cilindro circular: '))
        raio = float(input('Digite o raio do cilindro circular: '))
        v = 3.14 * (raio * raio) * altura #formula para calcular o volume do cilindro
    except ValueError:
        print('Apenas valores númericos serão aceitos...')
    else:
        print(f'O volume do cilindro é: {v:.2f}')
        break
