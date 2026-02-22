#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar:
# considere U$$ 1,00 = 3,27

#real = float(input('Quanto de dinhiro vc tem na carteira? R$'))
#dolar = real/5.22
#print('com tantos reais R$ {}, vc pode comprar tantos U$${}'.format (real, dolar))


#Faca um programa que leia a largura e altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2 metros quadrados. Sabendo que uma area de 2 metros leva 1 litro de tinta

largura =float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensao de {} e {} e sua area de {}'.format(largura,altura,area))
tinta = area/2
print('Para pintar essa parede, vc vai precisa de {} de tinta'.format(tinta))