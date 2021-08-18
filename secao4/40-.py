dia = 30.00
dia_trabalho = int(input('Quantos dias inteiros você trabalhou? '))
pagar = dia_trabalho * dia 
imposto = pagar - (pagar * 8/100)
saldo = imposto

print(f'Já com 8% de imposto você irá receber: {saldo:2f}')
