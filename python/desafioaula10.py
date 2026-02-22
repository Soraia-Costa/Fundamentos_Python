#Escreva um programa que faca o computador "pensar"em um numero inteiro entre 0 a 5 e peca para o usuario tentar descpbrir qual foi o numero escolhido pelo computador - O programa devera escrever na tela se o usuario venceu ou perdeu'''
'''from random import randint
computador = randint(0,5) 
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? '))
if jogador == computador:
    print('Parabens, vc acertou!!')
else:
    print('Computador ganhou!!')
print('Pensei no numero : {}'.format (computador))'''

#Escreva um program que leia a velocidade de um carro. Se ela ultrapassar 80 km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7.00 por cada km acima do limite


velocidade=float(input('Qual a velocidade do seu carro?'))
if velocidade > 80:
  print('Multado! Voce execedeu o limite permitido que é de 80 km/h')
  multa = (velocidade -80)* 7
  print('Voce deve paga uma multa de R${:.2f}!'.format (multa))
print('Tenha um bom dia! Dirija com segurança!')

 