while True:
    try:
        n = int(input('Digite um valor: '))
        sucessor_triplo = n * 3 + 1
        antecessor_do_dobro = n * 2 - 1
    except ValueError:
        print('Apenas valores inteiros serão aceitos...')
    else:
        print(f'Número lido: {n}')
        print(f'Soma do sucessor do triplo do número + o antecessor de seu número: {sucessor_triplo + antecessor_do_dobro}')
        break
