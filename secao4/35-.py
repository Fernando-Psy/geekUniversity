from math import sqrt

while True:
    try:
        a = int(input('Digite um valor inteiro: '))
        b = int(input('Digite outro valor inteiro: '))
        hipotenusa = sqrt((a*a) + (b*b))
    except ValueError:
        print('Apenas valores inteiros são aceitos... Digite novamente....')
    else:
        print(f'Valor da hipotenusa: {hipotenusa:.2f}')
        break
