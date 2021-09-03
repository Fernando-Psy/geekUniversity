dia = 30 # quanto a pessoa recebe por dia trabalhado
dia_trabalho = int(input('Quantos dias inteiros você trabalhou? '))
pagar = dia_trabalho * dia# quanto a empresa vai pagar dependendo da quantidade de dias trabalhados
imposto = pagar - (pagar * 8/100) # valor do imposto sobre quanto o funcionário irá receber
saldo = imposto # apenas o resultado do imposto

print(f'Já com 8% de imposto você irá receber: {saldo:.2f}')
