#Escreva um program que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar sabendo que o carro custa R$60,00 por dia e R$ 0,15 por  km rodado
dias = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos km foram rodados ?'))
pagar=dias *60 + (km*0.15)

print('O total à pagar é de R$ {:.2f}'.format(pagar))
