
while True: # gerando o loop infinito para só sair se não tiver nenhum error
    try: # testando o código
        n = int(input('Digite um valor: '))  
    except ValueError: #valor do erro
        print('Apenas números inteiros serão aceitos')
    else: # resultado se não tiver errros
        print(f'Número digitado: {n}')
        break
