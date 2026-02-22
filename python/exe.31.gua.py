#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

'''distancia =float(input('Qual a distancia da sua viagem?'))
print('Voce esta prestes a comecar uma viagem de {:.2f}km'.format (distancia))
if distancia  <= 200:
  preco = distancia *0.50
 
else:
    preco = distancia *0.45
print('Voce ira pagar nessa viagem R$ {:.2f}'.format(preco))
  
print('Tenha uma boa viagem !!')'''


distancia = float(input('Qual é a distancia da sua viagem? '))
print('Voce esta prestes a comecar uma viagem de {} km'.format(distancia))
preco = distancia*0.50 if distancia<=200 else distancia*0.45
print ('O preco da sua passagem sera de R$ {:.2f}'.format(preco))
      