while True: # grando um loop infinito, até a pessoa digitar uma letra, maiúsucla ou mínuscula
    letra = input('Digite uma letra: ').strip().upper()
    #tupla com o alfabeto já que não vou mudar os valores(valores fixos)
    alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    if letra not in alfabeto:#se a letra não estiver na tupla, vai mandar a pessoa escrever outro valor
        print(f'Digite uma letra do alfabeto')
    else:
        print(f'Letra em maiúsculo? {letra.upper()}')
        print(f'Letra em minúsculo: {letra.lower()}') # esse valor só será exibido se for uma letra
        break
